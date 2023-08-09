from django.db import models
from offer.models import Training, Offer
from airport.models import Airport


class Client(models.Model):
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
        max_length=20, help_text="Email of client", null=True, blank=True
    )
    address = models.CharField(max_length=200, help_text="Address of client")
    phone_no = models.IntegerField(help_text="Phone no. of client")
    training = models.ManyToManyField(
        Training, blank=True, help_text="If client was on training, training name"
    )
    offer = models.ManyToManyField(
        Offer, blank=True, help_text="If client uses the offer, offer name"
    )
    aeroclub_meber = models.BooleanField(
        help_text="Information if client is a Aeroclub member"
    )
