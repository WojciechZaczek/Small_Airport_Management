from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta


@login_required(login_url="/login/")
def home(request):
    return render(request, "dashboard/dashboard.html", {"title": "Home"})
