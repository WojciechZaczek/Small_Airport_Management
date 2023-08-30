from django import forms
from .models import Department, Company


class CreatCompany(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Company name", "class": "form-control"}
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Company address", "class": "form-control"}
        )
    )
    telephone = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Company telephone number", "class": "form-control"}
        )
    )
    email_domina = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Company email domina", "class": "form-control"}
        )
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Company description", "class": "form-control"}
        )
    )

    class Meta:
        model = Company
        fields = ["name", "address", "telephone", "email_domina", "description"]


class CreatDepartment(forms.ModelForm):
    name = forms.ChoiceField(
        choices=Department.DEPARTAMENT,
        widget=forms.Select(
            attrs={"placeholder": "Department", "class": "form-control"}
        ),
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Department description", "class": "form-control"}
        )
    )

    company_id = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        widget=forms.TextInput(
            attrs={"placeholder": "Airport ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = Department
        fields = ["name", "description", "company_id"]
