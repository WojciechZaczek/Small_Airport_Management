from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserLoginForm, UserRegisterForm
from .models import CustomUser, Worker


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm

    model = CustomUser

    fieldsets = (
        *UserAdmin.fieldsets,
        ("Additional information", {"fields": ("department", "job_position")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Worker)
