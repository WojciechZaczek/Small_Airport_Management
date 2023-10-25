from django.db import models
from offer.models import Training, Offer
from organization.models import Company
from django.core.exceptions import ValidationError
from django.urls import reverse


class Client(models.Model):
    corporate_client = models.BooleanField(
        help_text="If client is a corporate - Yes/No"
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
        max_length=20, help_text="Email of client", null=True, blank=True
    )
    address = models.CharField(max_length=200, help_text="Address of client")
    phone_no = models.IntegerField(help_text="Phone no. of client")
    training = models.ManyToManyField(
        Training,
        blank=True,
        help_text="If client was on training, training name",
    )
    offer = models.ManyToManyField(
        Offer, blank=True, help_text="If client uses the offer, offer name"
    )
    aeroclub_meber = models.BooleanField(
        help_text="Information if client is a Aeroclub member"
    )
    company_id = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        help_text="Company ID - information which organization client is it",
    )

    def clean(self):
        if self.corporate_client and not self.company_name:
            raise ValidationError("Corporate name must must be provided")
        if self.corporate_client and not self.nip:
            raise ValidationError("Nip name must must be provided")
        if not self.corporate_client and not self.name:
            raise ValidationError("Name must must be provided")

        if not self.corporate_client and not self.last_name:
            raise ValidationError("Last name must must be provided")

        if not self.corporate_client and not self.pesel:
            raise ValidationError("Pesel must must be provided")

        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("clients_detail", kwargs={"pk": self.pk})
