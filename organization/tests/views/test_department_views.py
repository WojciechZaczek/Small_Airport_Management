from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from organization.factories import CompanyFactory, DepartmentFactory
from airport.factories import AirportFactory


class DepartmentCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)

    def test_view_departments_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("departments_add"))
        self.assertTemplateUsed(response, "organization/departments_form.html")

    def test_view_departments_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("departments_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/organizations/departments/new/")


class DepartmentUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create(name="Test company")
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)

    def test_view_departments_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("departments_update", kwargs={"pk": self.department.pk})
        )
        self.assertTemplateUsed(response, "organization/departments_form.html")

    def test_view_departments_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("departments_update", kwargs={"pk": self.department.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "/login/?next=/organizations/departments/1/update/"
        )


class DepartmentDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create(name="Test company")
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)

    def test_view_departments_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("departments_delete", kwargs={"pk": self.department.pk})
        )
        self.assertTemplateUsed(response, "organization/departments_delete.html")

    def test_view_departments_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("departments_delete", kwargs={"pk": self.department.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "/login/?next=/organizations/departments/1/delete/"
        )
