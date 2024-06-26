from django.db import models
from airport.constants import SURFACE
from airport.models import Hangar, OutsideAircraftStand, Airport
from clients.models import Client
from django.core.exceptions import ValidationError
from django.urls import reverse


class Aircraft(models.Model):
    AIRCRAFT_TYPES = (
        ("A", "Airplane"),
        ("H", "Helicopter"),
        ("AS", "Airship"),
        ("G", "Glider"),
        ("P", "Paramotor"),
        ("B", "Balloon"),
        ("UAV", "Unmanned Aerial Vehicle"),
    )
    manufacture = models.CharField(max_length=50, help_text="Name op aircraft producer")
    name = models.CharField(max_length=50, help_text="Aircraft name or no")
    type = models.CharField(
        choices=AIRCRAFT_TYPES, max_length=3, help_text="Type of Aircraft, from list"
    )
    take_off_ground = models.IntegerField(
        help_text="Take off first part, where aircraft is on the ground in meters"
    )
    take_off_over_50ft_distance = models.IntegerField(
        help_text="Take off second part, from where the vehicle leaves the ground to until it reaches 50 ft in meters"
    )
    landing_groundroll = models.IntegerField(
        help_text="aircraft landing distance - on the ground in meters"
    )
    fuel_capacity = models.IntegerField(help_text="Aircraft fuel capacity")
    runway_surface_type = models.CharField(
        max_length=50, choices=SURFACE, help_text="Surface that aircraft can land"
    )
    description = models.TextField(
        max_length=500, help_text="Important information about aircraft"
    )

    @property
    def take_off_distance(self):
        return self.take_off_ground + self.take_off_over_50ft_distance

    def can_land_at_airport(self, runways):
        return any(self.landing_groundroll <= runway.LDA for runway in runways)

    def get_absolute_url(self):
        return reverse("aircrafts_details", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.manufacture} {self.name}"


class AircraftHangared(models.Model):
    aircraft = models.ForeignKey(
        Aircraft, on_delete=models.CASCADE, help_text="Aircraft ID"
    )
    aircraft_registration_no = models.CharField(
        max_length=50, help_text="Registration no", null=True, blank=True
    )
    airport_property = models.BooleanField(
        help_text="Information if airport is the owner of this aircraft"
    )
    hangar = models.ForeignKey(
        Hangar, on_delete=models.CASCADE, help_text="Hangar ID", null=True, blank=True
    )

    outside_stand = models.ForeignKey(
        OutsideAircraftStand,
        on_delete=models.CASCADE,
        help_text="Outside stand ID",
        null=True,
        blank=True,
    )
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Aiport ID", null=True, blank=True
    )
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, help_text="Client ID", null=True, blank=True
    )

    def clean(self):
        if not self.hangar and not self.outside_stand:
            raise ValidationError(
                "At least one of hangar_id or outside_stand_id must be provided"
            )

        if self.hangar and self.outside_stand:
            raise ValidationError(
                "Only one of hangar_id or outside_stand_id can be set"
            )

        if not self.client and not self.airport_property:
            raise ValidationError(
                "At least one of client_id or airport_property must be provided"
            )

        if self.client and self.airport_property:
            raise ValidationError("Only on of client_id or airport_property can be set")

        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("aircrafts_hangared_details", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.aircraft}"
