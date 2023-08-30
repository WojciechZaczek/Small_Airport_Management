from django import forms
from .models import Runway, Airport
from .constants import SURFACE, TYPES_OF_TRAFFIC_PERMISSION


class CreatAirport(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Airport Name", "class": "form-control"}
        )
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Airport city", "class": "form-control"}
        )
    )

    address = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Runway Address", "class": "form-control"}
        )
    )

    types_of_traffic_permitted = forms.ChoiceField(
        choices=TYPES_OF_TRAFFIC_PERMISSION,
        widget=forms.Select(
            attrs={"placeholder": "Types of traffic permitted", "class": "form-control"}
        ),
    )

    radio = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Radio frequency", "class": "form-control"}
        )
    )
    elevation = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Airport elevation", "class": "form-control"}
        )
    )
    co_ordinates = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Airport coordinates", "class": "form-control"}
        )
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Airport description", "class": "form-control"}
        )
    )
    length = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Airport length", "class": "form-control"}
        )
    )
    width = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Airport width", "class": "form-control"}
        )
    )
    square_meters = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"placeholder": "Airport square meters", "class": "form-control"}
        )
    )

    API = forms.FileField(
        widget=forms.FileInput(attrs={"placeholder": "API", "class": "form-control"})
    )

    class Meta:
        model = Airport
        fields = [
            "name",
            "city",
            "address",
            "types_of_traffic_permitted",
            "radio",
            "elevation",
            "co_ordinates",
            "description",
            "length",
            "width",
            "square_meters",
            "API",
        ]


class CreatRunway(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Runway Name", "class": "form-control"}
        )
    )

    length = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Runway Length", "class": "form-control"}
        )
    )
    width = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Runway Width", "class": "form-control"}
        )
    )
    surface = forms.ChoiceField(
        choices=SURFACE,
        widget=forms.Select(
            attrs={"placeholder": "Runway Surface", "class": "form-control"}
        ),
    )

    light = forms.BooleanField(required=False)
    markings = forms.BooleanField(required=False)
    TORA = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Runway  TORA", "class": "form-control"}
        )
    )
    LDA = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Runway LDA", "class": "form-control"}
        )
    )
    CWY = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Runway CWY", "class": "form-control"}
        )
    )
    SWY = forms.FloatField(
        widget=forms.TextInput(
            attrs={"placeholder": "Runway SWY", "class": "form-control"}
        )
    )
    airport_id = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Airport ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = Runway
        fields = [
            "name",
            "length",
            "width",
            "surface",
            "light",
            "markings",
            "TORA",
            "LDA",
            "CWY",
            "SWY",
            "airport_id",
        ]
