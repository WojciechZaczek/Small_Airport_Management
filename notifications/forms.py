from django import forms

from airport.models import Airport
from .models import Notification


class CreateNotification(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Notification title", "class": "form-control"}
        )
    )

    view_date = forms.DateField(
        widget=forms.TextInput(
            attrs={"placeholder": "Notification view date", "class": "form-control"}
        )
    )

    content = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Notification text", "class": "form-control"}
        )
    )

    airport = forms.ModelChoiceField(
        queryset=Airport.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Choose an Airport",
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(CreateNotification, self).__init__(*args, **kwargs)

        if user:
            self.fields["airport"].queryset = Airport.objects.filter(
                company=user.company
            )

    class Meta:
        model = Notification
        fields = ["title", "view_date", "content", "airport"]
