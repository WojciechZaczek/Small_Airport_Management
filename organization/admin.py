from django.contrib import admin

from .models import Department, Company, Worker


admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Worker)
