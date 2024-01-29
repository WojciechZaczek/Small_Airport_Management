from django import forms

from .models import Training, Offer
from organization.models import Worker
from airport.models import Airport


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
        queryset=Worker.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Choose an Worker",
    )
    airport = forms.ModelChoiceField(
        queryset=Airport.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Choose an Airport",
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(CreateTraining, self).__init__(*args, **kwargs)

        if user:
            self.fields["worker"].queryset = Worker.objects.filter(company=user.company)
            self.fields["airport"].queryset = Airport.objects.filter(
                company=user.company
            )

    class Meta:
        model = Training
        fields = ["name", "price", "description", "hours", "worker", "airport"]


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

    airport = forms.ModelChoiceField(
        queryset=Airport.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Choose an Airport",
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(CreateOffer, self).__init__(*args, **kwargs)

        if user:
            self.fields["airport"].queryset = Airport.objects.filter(
                company=user.company
            )

    class Meta:
        model = Offer
        fields = ["name", "price", "description", "airport"]
