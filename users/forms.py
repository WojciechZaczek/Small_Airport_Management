from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from django.contrib.auth.models import Group
from django import forms
from .models import CustomUser
from organization.models import Company
from organization.models import Department


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

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

    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        widget=forms.Select(attrs={"placeholder": "Company", "class": "form-control"}),
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        self.update_user_group(user)

        return user

    def update_user_group(self, user):
        group_name = self.cleaned_data.get("job_position")
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            group = None

        if group and group not in user.groups.all():
            user.groups.clear()
            user.groups.add(group)
