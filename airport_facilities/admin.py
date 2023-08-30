from django.contrib import admin

from .models import Building, Vehicle, Property, Others

admin.site.register(Building)
admin.site.register(Others)
admin.site.register(Vehicle)
admin.site.register(Property)
