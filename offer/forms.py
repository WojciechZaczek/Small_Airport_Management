from django import forms

from .models import Training, Offer
from organization.models import Worker


class CreateTraining(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Training Name", "class": "form-control"}
        )
    )

    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Training Price", "class": "form-control"}
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Training description", "class": "form-control"}
        )
    )
    hours = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Training length in hours", "class": "form-control"}
        )
    )

    worker = forms.ModelChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Worker ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = Training
        fields = [
            "name",
            "price",
            "description",
            "hours",
            "worker",
        ]


class CreateOffer(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Training Name", "class": "form-control"}
        )
    )

    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Training Price", "class": "form-control"}
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Training description", "class": "form-control"}
        )
    )

    class Meta:
        model = Offer
        fields = ["name", "price", "description"]
