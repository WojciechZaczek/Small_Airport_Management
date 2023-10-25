from django import forms

from .models import Building, Vehicle, Others, Property
from organization.models import Department


class CreateBuilding(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Building Name", "class": "form-control"}
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Building description", "class": "form-control"}
        )
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Department ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = Building
        fields = ["name", "department", "description"]


class CreateVehicle(forms.ModelForm):
    type = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Vehicle Type", "class": "form-control"}
        )
    )

    registration_no = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Vehicle Name", "class": "form-control"}
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Vehicle description", "class": "form-control"}
        )
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Department ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = Vehicle
        fields = ["type", "registration_no", "department", "description"]


class CreateProperty(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Property Name", "class": "form-control"}
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Property description", "class": "form-control"}
        )
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Property ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = Property
        fields = ["name", "department", "description"]


class CreateOthers(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Other Name", "class": "form-control"}
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Other description", "class": "form-control"}
        )
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Department ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = Others
        fields = ["name", "department", "description"]
