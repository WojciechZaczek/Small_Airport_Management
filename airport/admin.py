from django.contrib import admin

from .models import Airport, Runway, Hangar, OutsideAircraftStand

admin.site.register(Airport)
admin.site.register(Runway)
admin.site.register(Hangar)
admin.site.register(OutsideAircraftStand)
