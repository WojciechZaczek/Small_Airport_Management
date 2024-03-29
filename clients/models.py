from django.db import models
from offer.models import Training, Offer
from organization.models import Company
from django.core.exceptions import ValidationError
from django.urls import reverse


class Client(models.Model):
    corporate_client = models.BooleanField(
        help_text="If client is a corporate - Yes/No", blank=True
    )
    name = models.CharField(
        max_length=20, help_text="Name of client", null=True, blank=True
    )
    last_name = models.CharField(
        max_length=20, help_text="Last name of client", null=True, blank=True
    )
    pesel = models.IntegerField(help_text=" Pesel of client", null=True, blank=True)
    company_name = models.CharField(
        max_length=20,
        help_text="If client is a company, name of company",
        null=True,
        blank=True,
    )
    nip = models.IntegerField(
        help_text="If client is a company, NIP of company", null=True, blank=True
    )
    email = models.CharField(
        max_length=50, help_text="Email of client", null=True, blank=True
    )

    phone_no = models.IntegerField(help_text="Phone no. of client")
    training = models.ManyToManyField(
        Training,
        blank=True,
        help_text="If client was on training, training name",
    )
    offer = models.ManyToManyField(
        Offer,
        blank=True,
        help_text="If client uses the offer, offer name",
    )
    aeroclub_meber = models.BooleanField(
        help_text="Information if client is a Aeroclub member"
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        help_text="Company ID - information which organization client is it",
        related_name="clients",
    )

    # def save(self, *args, **kwargs):
    #     self.clean()
    # super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("clients_details", kwargs={"pk": self.pk})

    def __str__(self):
        if not self.corporate_client:
            return f"{self.name} {self.last_name}"
        else:
            return f"{self.company_name}"
