from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification
from airport.models import Airport
from .forms import CreateNotification


@login_required()
def notifications(request):
    users_airport = Airport.objects.filter(company=request.user.company).first()
    all_notifications = Notification.objects.filter(airport=users_airport).order_by(
        "view_date"
    )

    today = timezone.localdate()
    todays_notifications = [n for n in all_notifications if n.view_date == today]
    past_notifications = [n for n in all_notifications if n.view_date < today]
    future_notifications = [n for n in all_notifications if n.view_date > today]

    return render(
        request,
        "notifications/notifications.html",
        {
            "title": "Notifications",
            "todays_notifications": todays_notifications,
            "past_notifications": past_notifications,
            "future_notifications": future_notifications,
        },
    )


class NotificationsDetailView(LoginRequiredMixin, DetailView):
    model = Notification
    template_name = "notifications/notifications_details.html"


class NotificationsCreateView(LoginRequiredMixin, CreateView):
    model = Notification
    template_name = "notifications/notifications_form.html"

    form_class = CreateNotification

    def form_valid(self, form):
        user = self.request.user
        airports = Airport.objects.filter(company=user.company)
        author = user
        form.instance.author = author
        if airports.exists():
            form.instance.airport = airports.first()
        return super().form_valid(form)


class NotificationsUpdateView(LoginRequiredMixin, UpdateView):
    model = Notification
    template_name = "notifications/notifications_form.html"

    form_class = CreateNotification


class NotificationsDeleteView(LoginRequiredMixin, DeleteView):
    model = Notification
    template_name = "notifications/notifications_delete.html"
    success_url = reverse_lazy("notifications")
