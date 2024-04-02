from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from organization.factories import CompanyFactory, DepartmentFactory
from airport.factories import AirportFactory
from organization.models import Department


class DepartmentCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.new_department_data = {
            "name": "IT",
            "description": "New test description",
            "company": self.company.pk,
        }

    def test_view_departments_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("departments_add"))
        self.assertTemplateUsed(response, "organization/departments_form.html")

    def test_view_departments_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("departments_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/organizations/departments/new/")

    def test_view_departments_create_creates_new_department_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Department.objects.count(), 0)
        response = self.client.post(
            reverse("departments_add"), self.new_department_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Department.objects.count(), 1)

    def test_view_departments_create_creates_new_department_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("departments_add"), self.new_department_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_department = Department.objects.first()
        self.assertEqual(new_department.description, "New test description")


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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response,
            f"/login/?next=/organizations/departments/{self.department.pk}/update/",
        )

    def test_view_departments_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "name": "IT",
            "description": "New test description",
            "company": self.company.pk,
        }
        response = self.client.post(
            reverse("departments_update", kwargs={"pk": self.department.pk}),
            data=update,
        )
        print(response.content)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        self.department.refresh_from_db()
        self.assertEqual(self.department.description, update["description"])


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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response,
            f"/login/?next=/organizations/departments/{self.department.pk}/delete/",
        )

    def test_departments_delete_view_deletes_department_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Department.objects.count(), 1)
        response = self.client.delete(
            reverse("departments_delete", kwargs={"pk": self.department.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Department.objects.count(), 0)
