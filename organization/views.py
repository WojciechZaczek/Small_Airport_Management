from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Company, Department

from .forms import CreatDepartment, CreatCompany


def company(request):
    return render(
        request,
        "organization/organization.html",
        {
            "organization": Company.objects.filter(name=request.user.company_id),
            "department": Department.objects.filter(company_id=request.user.company_id),
        },
    )


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = "organization/company_form.html"

    form_class = CreatCompany
    success_url = reverse_lazy("organization")


class DepartmentCreateView(CreateView):
    model = Department
    template_name = "organization/department_form.html"

    form_class = CreatDepartment
    success_url = reverse_lazy("organization")


class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = "organization/department_form.html"

    form_class = CreatDepartment
    success_url = reverse_lazy("organization")


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "organization/department_delete.html"
    success_url = reverse_lazy("organization")
