from django import forms
from offer.models import Offer
from offer.models import Training
from django.core.exceptions import ValidationError

from .models import Client


class CreatClients(forms.ModelForm):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Client's name", "class": "form-control"}
        ),
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Client's last name", "class": "form-control"}
        ),
    )

    pesel = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Client's pesel", "class": "form-control"}
        ),
    )

    company_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Client's company name", "class": "form-control"}
        ),
    )

    nip = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Client's NIP", "class": "form-control"}
        ),
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Client's email", "class": "form-control"}
        )
    )

    phone_no = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Client's phone no.", "class": "form-control"}
        )
    )

    training = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Training.objects.all(),
        widget=forms.SelectMultiple(
            attrs={"placeholder": "Training client attends", "class": "form-control"}
        ),
    )

    offer = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Offer.objects.all(),
        widget=forms.SelectMultiple(
            attrs={"placeholder": "Offer client attends", "class": "form-control"}
        ),
    )

    aeroclub_meber = forms.BooleanField(required=False)

    class Meta:
        model = Client
        fields = [
            "name",
            "last_name",
            "pesel",
            "company_name",
            "nip",
            "email",
            "phone_no",
            "training",
            "offer",
            "aeroclub_meber",
        ]

    def clean(self):
        cleaned_data = super(CreatClients, self).clean()

        if bool(self.data.get("corporate_client")):
            if not cleaned_data["company_name"]:
                raise ValidationError("Corporate name must be provided")
            if not cleaned_data["nip"]:
                raise ValidationError("NIP must be provided")
        else:
            if not cleaned_data["name"]:
                raise ValidationError("Name must be provided")
            if not cleaned_data["last_name"]:
                raise ValidationError("Last name must be provided")
            if not cleaned_data["pesel"]:
                raise ValidationError("Pesel must be provided")

        return cleaned_data
