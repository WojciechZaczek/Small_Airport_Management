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
        name="departments_add",
    ),
    path(
        "organizations/departments/<int:pk>/update/",
        DepartmentUpdateView.as_view(),
        name="departments_update",
    ),
    path(
        "organizations/departments/<int:pk>/delete/",
        DepartmentDeleteView.as_view(),
        name="departments_delete",
    ),
    path(
        "organizations/companies/<int:pk>/update",
        CompanyUpdateView.as_view(),
        name="company_update",
    ),
    path("workers/", WorkerListView.as_view(), name="workers"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="workers_details"),
    path("workers/new/", WorkerCreateView.as_view(), name="workers_add"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="workers_update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="workers_delete"),
]
