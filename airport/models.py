from django.db import models
from .constants import SURFACE, AIRCRAFT_STAND_SIZE, TYPES_OF_TRAFFIC_PERMISSION
from django.core.exceptions import ValidationError
from django.urls import reverse
from organization.models import Company


class Airport(models.Model):
    name = models.CharField(max_length=30, help_text="Name of the airport")
    city = models.CharField(max_length=30, help_text="Airport city")
    address = models.TextField(max_length=200, help_text="Airport address")
    contact = models.TextField(max_length=200, help_text="Phone no.")
    types_of_traffic_permitted = models.CharField(
        choices=TYPES_OF_TRAFFIC_PERMISSION,
        help_text="Type of traffic permission - one type or two types",
        max_length=3,
    )
    radio = models.FloatField(help_text="Radio frequency")
    elevation = models.IntegerField(help_text="Airport elevation in ft")
    co_ordinates = models.TextField(
        max_length=200, help_text="ARP - coordinates and site at AD"
    )
    description = models.TextField(
        max_length=300, help_text="Other information about Information"
    )
    length = models.IntegerField(help_text="Airport length")
    width = models.IntegerField(help_text="Airport width")
    square_meters = models.IntegerField(help_text="Airport square meters")
    AIP = models.FileField(
        upload_to="uploads/AIP",
        help_text="AIP – Aeronautical Information Publication",
        blank=True,
        null=True,
    )

    company_id = models.ForeignKey(
        Company, on_delete=models.CASCADE, help_text="Company ID"
    )

    def __str__(self):
        return self.name


class Runway(models.Model):
    name = models.CharField(max_length=30, help_text="Name of the Runway")
    length = models.FloatField(help_text="Runway length in meters")
    width = models.FloatField(help_text="Runway width in meters")
    surface = models.CharField(
        choices=SURFACE,
        help_text="Runway type of surface. From tuple SURFACE",
        max_length=100,
    )
    light = models.BooleanField(help_text="Installed lighting on a Runway - Yes/No")
    markings = models.BooleanField(help_text="Marks on a Runway - Yes/No")
    TORA = models.FloatField(help_text="Take-off run available in meters")
    LDA = models.FloatField(help_text="Landing distance available in meters")
    CWY = models.FloatField(help_text="Clearway in meters")
    SWY = models.FloatField(help_text="Stopway in meters")
    airport_id = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Airport ID"
    )

    @property
    def TODA(self):
        if self.CWY == 0:
            return self.TORA
        else:
            return self.TORA + self.CWY

    @property
    def ASDA(self):
        if self.SWY == 0:
            return self.TORA
        else:
            return self.TORA + self.SWY

    def get_absolute_url(self):
        return reverse("runways_detail", kwargs={"pk": self.pk})


class OutsideAircraftStand(models.Model):
    name = models.CharField(max_length=30, help_text="Name of the outside stand")
    surface = models.CharField(
        choices=SURFACE,
        help_text="Stand type of surface. From tuple SURFACE",
        max_length=100,
    )
    size = models.CharField(
        choices=AIRCRAFT_STAND_SIZE,
        help_text="Stand size. From tuple AIRCRAFT_STAND_SIZE",
        max_length=100,
    )
    taken = models.BooleanField(help_text="Information if this stand is taken")

    airport_id = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Airport ID"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("outside_stands_details", kwargs={"pk": self.pk})


class Hangar(models.Model):
    name = models.CharField(max_length=30, help_text="Name of the hangar")
    hangar_height = models.FloatField(help_text="Hangar height in stand space")
    hangar_wight = models.FloatField(help_text="Hangar wight in stand space")
    doors_height = models.FloatField(help_text="Hangars doors height")
    doors_wight = models.FloatField(help_text="Hangars doors wight")
    small_stands_no = models.IntegerField(
        help_text="How many small stands are in Hangar"
    )
    small_stands_taken = models.IntegerField(
        help_text="How many small stands are in Hangar are taken"
    )

    airport_id = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Airport ID"
    )

    def clean(self):
        if self.small_stands_no < self.small_stands_taken:
            raise ValidationError("Not enough free stands")

        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("hangars_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
