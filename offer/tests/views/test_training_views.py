from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from offer.factories import TrainingFactory
from airport.factories import AirportFactory
from organization.factories import WorkerFactory
from offer.models import Training


class TrainingsViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.training = TrainingFactory.create(
            name="Training one", airport=self.airport
        )

    def test_view_trainings_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("trainings"))
        self.assertTemplateUsed(response, "offer/trainings.html")

    def test_view_trainings_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("trainings"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/trainings/")

    def test_view_trainings_returns_correct_offer_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("trainings"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Training one")

    def test_trainings_view_displayed_offer_price(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("trainings"))
        self.assertContains(response, self.training.price)


class TrainingsDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.training = TrainingFactory.create(airport=self.airport)

    def test_view_trainings_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("trainings_details", kwargs={"pk": self.training.pk})
        )
        self.assertTemplateUsed(response, "offer/trainings_details.html")

    def test_view_trainings_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("trainings_details", kwargs={"pk": self.training.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/trainings/{self.training.pk}/")

    def test_trainings_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("trainings_details", kwargs={"pk": self.training.pk})
        )
        self.assertContains(response, self.training.name)

    def test_trainings_details_price_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("trainings_details", kwargs={"pk": self.training.pk})
        )
        self.assertContains(response, self.training.price)

    def test_trainings_details_description_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("trainings_details", kwargs={"pk": self.training.pk})
        )
        self.assertContains(response, self.training.description)

    def test_trainings_details_worker_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("trainings_details", kwargs={"pk": self.training.pk})
        )
        self.assertContains(response, self.training.worker)

    def test_trainings_details_hours_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("trainings_details", kwargs={"pk": self.training.pk})
        )
        self.assertContains(response, self.training.hours)


class TrainingsCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.worker = WorkerFactory.create(company=self.user.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.new_training_data = {
            "name": "Alfa Training",
            "price": 100.00,
            "description": "Test description",
            "hours": 100,
            "worker": self.worker.pk,
            "airport": self.airport.pk,
        }

    def test_view_trainings_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("trainings_add"))
        self.assertTemplateUsed(response, "offer/trainings_form.html")

    def test_view_trainings_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("trainings_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/trainings/new/")

    def test_view_trainings_create_creates_new_training_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Training.objects.count(), 0)
        response = self.client.post(reverse("trainings_add"), self.new_training_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Training.objects.count(), 1)

    def test_view_trainings_create_creates_new_training_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(reverse("trainings_add"), self.new_training_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_training = Training.objects.first()
        self.assertEqual(new_training.name, "Alfa Training")


class TrainingsUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.worker = WorkerFactory.create(company=self.user.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.training = TrainingFactory.create(airport=self.airport)

    def test_view_trainings_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("trainings_update", kwargs={"pk": self.training.pk})
        )
        self.assertTemplateUsed(response, "offer/trainings_form.html")

    def test_view_trainings_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("trainings_update", kwargs={"pk": self.training.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/trainings/{self.training.pk}/update/"
        )

    def test_view_trainings_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "name": "Alfa Training",
            "price": self.training.price,
            "description": self.training.description,
            "hours": self.training.hours,
            "worker": self.worker.pk,
            "airport": self.airport.pk,
        }
        response = self.client.post(
            reverse("trainings_update", kwargs={"pk": self.training.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.training.refresh_from_db()
        self.assertEqual(self.training.name, update["name"])


class TrainingsDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.training = TrainingFactory.create(airport=self.airport)

    def test_view_trainings_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("trainings_delete", kwargs={"pk": self.training.pk})
        )
        self.assertTemplateUsed(response, "offer/trainings_delete.html")

    def test_view_trainings_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("trainings_delete", kwargs={"pk": self.training.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/trainings/{self.training.pk}/delete/"
        )
