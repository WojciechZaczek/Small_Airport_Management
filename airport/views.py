from django.shortcuts import render


def home(request):
    return render(
        request,
        "airport/../dashboard/templates/dashboard/home/index.html",
        {"title": "Home"},
    )
