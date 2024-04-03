from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from organization.factories import CompanyFactory, DepartmentFactory, WorkerFactory
from airport.factories import AirportFactory
from organization.models import Worker


class WorkerListViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)
        self.worker = WorkerFactory.create(company=self.company, first_name="Testowy")

    def test_view_workers_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("workers"))
        self.assertTemplateUsed(response, "organization/workers.html")

    def test_view_workers_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("workers"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/workers/")

    def test_view_workers_returns_correct_offer_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("workers"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Testowy")

    def test_workers_view_displayed_offer_last_name(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("workers"))
        self.assertContains(response, self.worker.last_name)


class WorkersDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)
        self.worker = WorkerFactory.create(company=self.company)

    def test_view_workers_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("workers_details", kwargs={"pk": self.worker.pk})
        )
        self.assertTemplateUsed(response, "organization/workers_details.html")

    def test_view_workers_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("workers_details", kwargs={"pk": self.worker.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/workers/{self.worker.pk}/")

    def test_workers_details_first_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("workers_details", kwargs={"pk": self.worker.pk})
        )
        self.assertContains(response, self.worker.first_name)

    def test_workers_details_last_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("workers_details", kwargs={"pk": self.worker.pk})
        )
        self.assertContains(response, self.worker.last_name)

    # def test_workers_details_department_content_displayed(self):
    #     self.client.force_login(self.user)
    #     response = self.client.get(
    #         reverse("workers_details", kwargs={"pk": self.worker.pk})
    #     )
    #     self.assertContains(response, self.worker.department)

    def test_workers_details_job_address_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("workers_details", kwargs={"pk": self.worker.pk})
        )
        self.assertContains(response, self.worker.address)

    def test_workers_details_phone_no_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("workers_details", kwargs={"pk": self.worker.pk})
        )
        self.assertContains(response, self.worker.phone_no)

    def test_workers_details_information_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("workers_details", kwargs={"pk": self.worker.pk})
        )
        self.assertContains(response, self.worker.information)


class WorkersCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)
        self.new_worker_data = {
            "first_name": "Test",
            "last_name": "last name test",
            "department": "office",
            "job_position": "ceo",
            "address": "test address",
            "phone_no": "test phone_no",
            "information": "test information",
            "company": self.company.pk,
        }

    def test_view_workers_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("workers_add"))
        self.assertTemplateUsed(response, "organization/workers_form.html")

    def test_view_workers_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("workers_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/workers/new/")

    def test_view_workers_create_creates_new_worker_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Worker.objects.count(), 0)
        response = self.client.post(reverse("workers_add"), self.new_worker_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Worker.objects.count(), 1)

    def test_view_workers_create_creates_new_worker_object_with_correct_content(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("workers_add"), self.new_worker_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_worker = Worker.objects.first()
        self.assertEqual(new_worker.first_name, "Test")


class WorkersUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)
        self.worker = WorkerFactory.create(company=self.company)

    def test_view_workers_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("workers_update", kwargs={"pk": self.worker.pk})
        )
        self.assertTemplateUsed(response, "organization/workers_form.html")

    def test_view_workers_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("workers_update", kwargs={"pk": self.worker.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/workers/{self.worker.pk}/update/"
        )

    def test_view_workers_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "first_name": "Test",
            "last_name": self.worker.last_name,
            "department": "office",
            "job_position": "ceo",
            "address": self.worker.address,
            "phone_no": self.worker.phone_no,
            "information": self.worker.information,
            "company": self.company.pk,
        }
        response = self.client.post(
            reverse("workers_update", kwargs={"pk": self.worker.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.worker.refresh_from_db()
        self.assertEqual(self.worker.first_name, update["first_name"])


class WorkersDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)
        self.worker = WorkerFactory.create(company=self.company)

    def test_view_workers_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("workers_delete", kwargs={"pk": self.worker.pk})
        )
        self.assertTemplateUsed(response, "organization/workers_delete.html")

    def test_view_workers_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("workers_delete", kwargs={"pk": self.worker.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/workers/{self.worker.pk}/delete/"
        )

    def test_workers_delete_view_deletes_worker_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Worker.objects.count(), 1)
        response = self.client.delete(
            reverse("workers_delete", kwargs={"pk": self.worker.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Worker.objects.count(), 0)
