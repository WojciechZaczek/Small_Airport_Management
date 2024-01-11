from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from organization.factories import DepartmentFactory, WorkerFactory, CompanyFactory


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.company = CompanyFactory.create()
        self.department = DepartmentFactory.create()
        self.worker = WorkerFactory.create()

    def test_organizations_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("organizations")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_company_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("company_update", kwargs={"pk": self.company.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_departments_add_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("departments_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_departments_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("departments_delete", kwargs={"pk": self.department.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_departments_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("departments_update", kwargs={"pk": self.department.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_workers_url_returns_200_status_code_for_standard_get(self):
        urls = ["workers", "workers_add"]
        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_workers_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("workers_details", kwargs={"pk": self.worker.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_workers_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("workers_update", kwargs={"pk": self.worker.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_workers_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("workers_delete", kwargs={"pk": self.worker.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
