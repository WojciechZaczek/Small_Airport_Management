from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
import datetime
import notifications.views
from datetime import datetime
from users.factories import UserFactory
from notifications.factories import NotificationFactory
from airport.factories import AirportFactory
from notifications.models import Notification
from django.utils import timezone
import unittest
from unittest.mock import patch


class NotificationsViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)

        self.future_notification = NotificationFactory.create(
            title="Notification one",
            airport=self.airport,
            view_date=datetime.datetime(2011, 1, 1, 0, 0, 0),
        )
        self.past_notification = NotificationFactory.create(
            title="Notification two", airport=self.airport, view_date="2009-1-1"
        )
        self.todays_notification = NotificationFactory.create(
            title="Notification three", airport=self.airport, view_date="2010-1-1"
        )

    def test_view_notifications_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertTemplateUsed(response, "notifications/notifications.html")

    def test_view_notifications_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("notifications"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/notifications/")

    def test_view_notifications_returns_correct_notification_title_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Notification one")

    def test_notifications_view_displayed_notification_author(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertContains(response, self.past_notification.author)

    @patch("notifications.views.timezone")
    def test_notification_view_should_divide_notification_by_date_and_add_object_to_future_notifications(
        self, mock_timezone
    ):
        mock_timezone.localdate.return_value = datetime.date(2010, 1, 1)
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        notifications_by_airport = response.context["notifications_by_airport"]
        airport_notifications = notifications_by_airport.get(
            self.future_notification.airport
        )
        future_notifications = airport_notifications.get("future_notifications")
        self.assertEqual(len(future_notifications), 1)
        self.assertEqual(future_notifications[0], self.future_notification)

    @patch("notifications.views.timezone")
    def test_notification_view_should_divide_notification_by_date_and_add_object_to_past_notifications(
        self, mock_timezone
    ):
        mock_timezone.localdate.return_value = datetime.date(2010, 1, 1)
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        notifications_by_airport = response.context["notifications_by_airport"]
        airport_notifications = notifications_by_airport.get(
            self.past_notification.airport
        )
        past_notifications = airport_notifications.get("past_notifications")
        self.assertEqual(len(past_notifications), 1)
        self.assertEqual(past_notifications[0], self.past_notification)

    @patch("notifications.views.timezone")
    def test_notification_view_should_divide_notification_by_date_and_add_object_to_todays_notifications(
        self, mock_timezone
    ):
        mock_timezone.localdate.return_value = datetime.date(2010, 1, 1)
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        notifications_by_airport = response.context["notifications_by_airport"]
        airport_notifications = notifications_by_airport.get(
            self.todays_notification.airport
        )
        todays_notifications = airport_notifications.get("todays_notifications")
        self.assertEqual(len(todays_notifications), 1)
        self.assertEqual(todays_notifications[0], self.todays_notification)


class NotificationsDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.notification = NotificationFactory.create(airport=self.airport)

    def test_view_notifications_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("notifications_details", kwargs={"pk": self.notification.pk})
        )
        self.assertTemplateUsed(response, "notifications/notifications_details.html")

    def test_view_notifications_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("notifications_details", kwargs={"pk": self.notification.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/notifications/{self.notification.pk}/"
        )

    def test_notifications_details_title_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("notifications_details", kwargs={"pk": self.notification.pk})
        )
        self.assertContains(response, self.notification.title)

    def test_notifications_details_author_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("notifications_details", kwargs={"pk": self.notification.pk})
        )
        self.assertContains(response, self.notification.author)

    def test_notifications_details_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("notifications_details", kwargs={"pk": self.notification.pk})
        )
        self.assertContains(response, self.notification.content)


class NotificationsCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.new_notification_data = {
            "title": "Test Notification",
            "content": "Test content",
            "date_posted": "2021-05-01",
            "view_date": "2022-05-01",
            "airport": self.airport.pk,
        }

    def test_view_notifications_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications_add"))
        self.assertTemplateUsed(response, "notifications/notifications_form.html")

    def test_view_notifications_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("notifications_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/notifications/new/")

    def test_view_notifications_create_creates_new_notification_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Notification.objects.count(), 0)
        response = self.client.post(
            reverse("notifications_add"), self.new_notification_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Notification.objects.count(), 1)

    def test_view_notifications_create_creates_new_notification_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("notifications_add"), self.new_notification_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_notification = Notification.objects.first()
        self.assertEqual(new_notification.title, "Test Notification")


class NotificationsUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.notification = NotificationFactory.create(airport=self.airport)

    def test_view_notifications_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("notifications_update", kwargs={"pk": self.notification.pk})
        )
        self.assertTemplateUsed(response, "notifications/notifications_form.html")

    def test_view_notifications_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("notifications_update", kwargs={"pk": self.notification.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/notifications/{self.notification.pk}/update/"
        )

    def test_view_notifications_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "title": "Test Notification",
            "content": self.notification.content,
            "date_posted": self.notification.date_posted,
            "view_date": self.notification.view_date,
            "airport": self.airport.pk,
        }
        response = self.client.post(
            reverse("notifications_update", kwargs={"pk": self.notification.pk}),
            data=update,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.notification.refresh_from_db()
        self.assertEqual(self.notification.title, update["title"])


class NotificationsDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.notification = NotificationFactory.create(airport=self.airport)

    def test_view_notifications_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("notifications_delete", kwargs={"pk": self.notification.pk})
        )
        self.assertTemplateUsed(response, "notifications/notifications_delete.html")

    def test_view_notifications_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("notifications_delete", kwargs={"pk": self.notification.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/notifications/{self.notification.pk}/delete/"
        )

    def test_notifications_delete_view_deletes_notification_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Notification.objects.count(), 1)
        response = self.client.delete(
            reverse("notifications_delete", kwargs={"pk": self.notification.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Notification.objects.count(), 0)
