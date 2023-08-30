from django.shortcuts import render


def aircraft(request):
    return render(request, "aircraft/aircraft.html", {"title": "Aircraft"})
