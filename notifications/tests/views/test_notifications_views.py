from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from notifications.factories import NotificationFactory
from airport.factories import AirportFactory


class NotificationsViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.notification = NotificationFactory.create(
            title="Notification one", airport=self.airport
        )

    def test_view_notifications_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertTemplateUsed(response, "notifications/notifications.html")

    def test_view_notifications_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("notifications"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/notifications/")

    def test_view_notifications_returns_correct_notification_title_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Notification one")

    def test_notifications_view_displayed_notification_author(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications"))
        self.assertContains(response, self.notification.author)


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/notifications/1/")

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
        self.notification = NotificationFactory.create(airport=self.airport)

    def test_view_notifications_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("notifications_add"))
        self.assertTemplateUsed(response, "notifications/notifications_form.html")

    def test_view_notifications_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("notifications_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/notifications/new/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/notifications/1/update/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/notifications/1/delete/")
