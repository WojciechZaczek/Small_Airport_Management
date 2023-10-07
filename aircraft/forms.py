from django import forms
from .models import Aircraft, AircraftHangared
from airport.constants import SURFACE
from airport.models import Hangar, OutsideAircraftStand
from clients.models import Client


class CreatAircraft(forms.ModelForm):
    type = forms.ChoiceField(
        choices=Aircraft.AIRCRAFT_TYPES,
        widget=forms.Select(
            attrs={"placeholder": "Type of Aircraft", "class": "form-control"}
        ),
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft Name, Model no", "class": "form-control"}
        )
    )

    manufacture = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft manufacture", "class": "form-control"}
        )
    )

    take_off_ground = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft take off ground", "class": "form-control"}
        )
    )

    take_off_over_50ft_distance = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Aircraft take off 50ft distance",
                "class": "form-control",
            }
        )
    )

    landing_groundroll = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Aircraft landing ground roll",
                "class": "form-control",
            }
        )
    )

    fuel_capacity = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft fuel capacity", "class": "form-control"}
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft description", "class": "form-control"}
        )
    )
    runway_surface_type = forms.ChoiceField(
        choices=SURFACE,
        widget=forms.Select(
            attrs={
                "placeholder": "Types surface aircraft can land",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Aircraft
        fields = [
            "type",
            "manufacture",
            "name",
            "take_off_ground",
            "take_off_over_50ft_distance",
            "landing_groundroll",
            "fuel_capacity",
            "runway_surface_type",
            "description",
        ]


class CreatAircraftHangared(forms.ModelForm):
    aircraft_id = forms.ModelChoiceField(
        queryset=Aircraft.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft ID", "class": "form-control"}
        ),
    )

    aircraft_registration_no = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft registration no", "class": "form-control"}
        )
    )

    airport_property = forms.BooleanField(required=False)

    hangar_id = forms.ModelChoiceField(
        required=False,
        queryset=Hangar.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft ID", "class": "form-control"}
        ),
    )

    outside_stand_id = forms.ModelChoiceField(
        required=False,
        queryset=OutsideAircraftStand.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft ID", "class": "form-control"}
        ),
    )

    client_id = forms.ModelChoiceField(
        required=False,
        queryset=Client.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Aircraft ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = AircraftHangared
        fields = [
            "aircraft_id",
            "aircraft_registration_no",
            "airport_property",
            "hangar_id",
            "outside_stand_id",
            "client_id",
        ]
