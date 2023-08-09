from django.shortcuts import render


def organization(request):
    return render(request, "organization/organization.html", {"title": "Organization"})
