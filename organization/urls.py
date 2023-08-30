from django.urls import path
from . import views
from .views import (
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDeleteView,
    CompanyUpdateView,
)

urlpatterns = [
    path("organizations/", views.company, name="organizations"),
    path(
        "organizations/departments/new/",
        DepartmentCreateView.as_view(),
        name="department_add",
    ),
    path(
        "organizations/departments/<int:pk>/",
        DepartmentUpdateView.as_view(),
        name="department_update",
    ),
    path(
        "organizations/departmenst/delete/<int:pk>/",
        DepartmentDeleteView.as_view(),
        name="department_delete",
    ),
    path(
        "organizations/companies/<int:pk>/",
        CompanyUpdateView.as_view(),
        name="company_update",
    ),
]
