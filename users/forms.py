from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from django import forms
from .models import CustomUser
from organization.models import Company
from organization.models import Department


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )

    class Meta:
        model = CustomUser
        fields = ("username", "password")


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First name", "class": "form-control"}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last name", "class": "form-control"}
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

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "department",
            "job_position",
            "company",
        ]


class CreateUser(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First name", "class": "form-control"}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last name", "class": "form-control"}
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

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "department", "job_position"]
