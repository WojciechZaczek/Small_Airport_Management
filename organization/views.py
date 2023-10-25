from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Company, Department, Worker
from airport.models import Airport

from .forms import CreatDepartment, CreatCompany, CreatWorker


def company(request):
    return render(
        request,
        "organization/organization.html",
        {
            "organization": Company.objects.filter(name=request.user.company),
            "department": Department.objects.filter(company_id=request.user.company),
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


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    template_name = "organization/workers.html"
    context_object_name = "workers"

    def get_queryset(self):
        user = self.request.user
        workers = Worker.objects.filter(company=user.company)
        return workers


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    template_name = "organization/workers_details.html"


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    template_name = "organization/workers_form.html"

    form_class = CreatWorker

    def form_valid(self, form):
        company = self.request.user.company
        form.instance.company = company
        return super().form_valid(form)


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    template_name = "organization/workers_form.html"

    form_class = CreatWorker


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    template_name = "organization/workers_delete.html"
    success_url = reverse_lazy("workers")
