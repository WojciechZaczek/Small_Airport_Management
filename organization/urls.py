from django.urls import path
from . import views
from .views import (
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDeleteView,
    CompanyUpdateView,
    WorkerUpdateView,
    WorkerCreateView,
    WorkerDeleteView,
    WorkerDetailView,
    WorkerListView,
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
        "organizations/departments/delete/<int:pk>/",
        DepartmentDeleteView.as_view(),
        name="department_delete",
    ),
    path(
        "organizations/companies/<int:pk>/",
        CompanyUpdateView.as_view(),
        name="company_update",
    ),
    path("workers/", WorkerListView.as_view(), name="workers"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="workers_details"),
    path("workers/new/", WorkerCreateView.as_view(), name="workers_add"),
    path("workers/update/<int:pk>/", WorkerUpdateView.as_view(), name="workers_update"),
    path("workers/delete/<int:pk>/", WorkerDeleteView.as_view(), name="workers_delete"),
]
