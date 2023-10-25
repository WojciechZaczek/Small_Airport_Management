from django import forms


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

    class Meta:
        model = Notification
        fields = ["title", "view_date", "content"]
