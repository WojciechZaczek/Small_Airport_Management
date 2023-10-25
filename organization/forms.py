from django import forms
from .models import Department, Company, Worker


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
            attrs={"placeholder": "Company ID", "class": "form-control"}
        ),
    )

    class Meta:
        model = Department
        fields = ["name", "description", "company_id"]


class CreatWorker(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Workers first name", "class": "form-control"}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Workers last name", "class": "form-control"}
        )
    )

    department = forms.ChoiceField(
        choices=Department.DEPARTAMENT,
        widget=forms.Select(
            attrs={"placeholder": "Workers department", "class": "form-control"}
        ),
    )

    job_position = forms.ChoiceField(
        choices=Department.JOB_TITLES,
        widget=forms.Select(
            attrs={"placeholder": "Workers job position", "class": "form-control"}
        ),
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Workers address", "class": "form-control"}
        )
    )
    phone_no = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Workers telephone number", "class": "form-control"}
        )
    )

    information = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Information about worker", "class": "form-control"}
        )
    )

    class Meta:
        model = Worker
        fields = [
            "first_name",
            "last_name",
            "department",
            "job_position",
            "address",
            "phone_no",
            "information",
        ]
