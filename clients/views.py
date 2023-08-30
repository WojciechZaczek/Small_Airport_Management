from django.shortcuts import render


def clients_members(request):
    return render(request, "clients/clients.html", {"title": "Clients"})
