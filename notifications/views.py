from django.shortcuts import render
from .models import Notification


def notifications(request):
    return render(
        request, "notifications/notifications.html", {"title": "Notifications"}
    )
