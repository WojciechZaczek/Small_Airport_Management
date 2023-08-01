from django.contrib import admin

from .models import Department, Company


admin.site.register(Company)
admin.site.register(Department)
