from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from users.models import CustomUser
from organization.factories import CompanyFactory


class UserListViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.other_user = UserFactory.create(
            company=self.user.company, first_name="Test"
        )

    def test_view_users_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("users"))
        self.assertTemplateUsed(response, "users/users.html")

    def test_view_users_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/users/")

    def test_view_users_returns_correct_offer_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Test")

    def test_users_view_displayed_offer_last_name(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("users"))
        self.assertContains(response, self.user.last_name)


class UserDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.other_user = UserFactory.create(company=self.user.company)

    def test_view_users_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("users_details", kwargs={"pk": self.user.pk})
        )
        self.assertTemplateUsed(response, "users/users_details.html")

    def test_view_users_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("users_details", kwargs={"pk": self.user.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/users/1/")

    def test_users_details_first_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("users_details", kwargs={"pk": self.user.pk})
        )
        self.assertContains(response, self.user.first_name)

    def test_users_details_last_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("users_details", kwargs={"pk": self.user.pk})
        )
        self.assertContains(response, self.user.last_name)


class UserUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.other_user = UserFactory.create(company=self.user.company)

    def test_view_users_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("users_update", kwargs={"pk": self.user.pk}))
        self.assertTemplateUsed(response, "users/users_form.html")

    def test_view_users_update_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("users_update", kwargs={"pk": self.user.pk}))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/users/1/update/")

    def test_view_users_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "first_name": "Test Name",
            "last_name": self.other_user.last_name,
            "department": "office",
            "job_position": "ceo",
            "company": self.company.pk,
        }
        response = self.client.post(
            reverse("users_update", kwargs={"pk": self.other_user.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.other_user.refresh_from_db()
        self.assertEqual(self.other_user.first_name, update["first_name"])


class UserDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.other_user = UserFactory.create(company=self.user.company)

    def test_view_users_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("users_delete", kwargs={"pk": self.user.pk}))
        self.assertTemplateUsed(response, "users/users_delete.html")

    def test_view_users_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("users_delete", kwargs={"pk": self.user.pk}))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/users/1/delete/")

    def test_users_delete_view_deletes_user_object(self):
        self.client.force_login(self.user)
        self.assertEqual(CustomUser.objects.count(), 2)
        response = self.client.delete(
            reverse("users_delete", kwargs={"pk": self.other_user.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(CustomUser.objects.count(), 1)
