from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from clients.factories import ClientPrivateFactory, ClientCorporateFactory
from clients.models import Client
from airport.factories import AirportFactory
from offer.factories import TrainingFactory, OfferFactory
from organization.factories import CompanyFactory


class ClientListViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.client_private = ClientPrivateFactory.create(
            company=self.user.company, last_name="Testowy"
        )
        self.client_corporate = ClientCorporateFactory.create(
            company=self.user.company, company_name="Test Company"
        )

    def test_view_clients_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertTemplateUsed(response, "clients/clients.html")

    def test_view_clients_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/clients/")

    def test_view_clients_returns_correct_private_client_last_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Testowy")

    def test_view_clients_returns_correct_corporate_client_last_company_name_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Test Company")

    def test_view_clients_returns_correct_private_client_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.client_private.name)

    def test_view_clients_returns_correct_corporate_client_nip_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.client_corporate.nip)


class ClientsPrivateDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.client_private = ClientPrivateFactory.create(
            company=self.user.company,
        )

    def test_view_clients_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_private.pk})
        )
        self.assertTemplateUsed(response, "clients/clients_details.html")

    def test_view_clients_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_private.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/clients/1/")

    def test_clients_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_private.pk})
        )
        self.assertContains(response, self.client_private.name)

    def test_clients_details_last_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_private.pk})
        )
        self.assertContains(response, self.client_private.last_name)

    def test_clients_details_last_pesel_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_private.pk})
        )
        self.assertContains(response, self.client_private.pesel)

    def test_clients_details_last_phone_no_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_private.pk})
        )
        self.assertContains(response, self.client_private.phone_no)

    def test_clients_details_last_email_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_private.pk})
        )
        self.assertContains(response, self.client_private.email)


class ClientsCorporateDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.client_corporate = ClientCorporateFactory.create(
            company=self.user.company,
        )

    def test_view_clients_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertTemplateUsed(response, "clients/clients_details.html")

    def test_view_clients_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/clients/1/")

    def test_clients_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertContains(response, self.client_corporate.company_name)

    def test_clients_details_last_nip_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertContains(response, self.client_corporate.nip)

    def test_clients_details_last_phone_no_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertContains(response, self.client_corporate.phone_no)

    def test_clients_details_last_email_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_details", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertContains(response, self.client_corporate.email)


class NewClientViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()

    def test_view_clients_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients_add"))
        self.assertTemplateUsed(response, "clients/clients_new.html")

    def test_view_clients_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("clients_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/clients/new/")


class ClientsCorporateCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.offer = OfferFactory.create(airport=self.airport)
        self.training = TrainingFactory.create(airport=self.airport)
        self.new_corporate_client_data = {
            "corporate_client": True,
            "company_name": "Test company name",
            "nip": 39,
            "email": "Test email",
            "phone_no": 43432,
            "training": self.training.pk,
            "offer": self.offer.pk,
            "aeroclub_meber": True,
            "company": self.company.pk,
        }

    def test_view_client_corporate_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients_add_corporate"))
        self.assertTemplateUsed(response, "clients/clients_corporate_form.html")

    def test_view_client_corporate_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("clients_add_corporate"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/clients/new/corporate/")

    def test_view_client_corporate_create_creates_new_client_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Client.objects.count(), 0)
        response = self.client.post(
            reverse("clients_add_corporate"), self.new_corporate_client_data
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Client.objects.count(), 1)

    def test_view_client_corporate_create_creates_new_client_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("clients_add_corporate"), self.new_corporate_client_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_client = Client.objects.first()
        self.assertEqual(new_client.company_name, "Test company name")


class ClientsPrivateCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.offer = OfferFactory.create(airport=self.airport)
        self.training = TrainingFactory.create(airport=self.airport)
        self.new_private_client_data = {
            "corporate_client": False,
            "name": "Test name",
            "last_name": "Last name",
            "pesel": 39,
            "email": "Test email",
            "phone_no": 43432,
            "training": self.training.pk,
            "offer": self.offer.pk,
            "aeroclub_meber": True,
            "company": self.company.pk,
        }

    def test_view_client_private_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients_add_private"))
        self.assertTemplateUsed(response, "clients/clients_private_form.html")

    def test_view_client_private_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("clients_add_private"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/clients/new/private/")

    def test_view_client_private_create_creates_new_client_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Client.objects.count(), 0)
        response = self.client.post(
            reverse("clients_add_private"), self.new_private_client_data
        )
        form = response.context["form"]
        print(form.is_valid())
        print(form.errors)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Client.objects.count(), 1)

    def test_view_client_private_create_creates_new_client_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("clients_add_private"), self.new_private_client_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_client = Client.objects.first()
        self.assertEqual(new_client.name, "Test name")


class ClientsUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.offer = OfferFactory.create(airport=self.airport)
        self.training = TrainingFactory.create(airport=self.airport)
        self.client_private = ClientPrivateFactory.create(company=self.user.company)
        self.client_corporate = ClientCorporateFactory.create(company=self.user.company)

    def test_view_clients_corporate_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_update", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertTemplateUsed(response, "clients/clients_form.html")

    def test_view_clients_private_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_update", kwargs={"pk": self.client_private.pk})
        )
        self.assertTemplateUsed(response, "clients/clients_form.html")

    def test_view_clients_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("clients_update", kwargs={"pk": self.client_private.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/clients/1/update/")

    def test_view_client_update_changes_private_client_object_content(self):
        self.client.force_login(self.user)
        update = {
            "corporate_client": False,
            "name": "Test name",
            "last_name": self.client_private.last_name,
            "pesel": self.client_private.pesel,
            "email": self.client_private.email,
            "phone_no": self.client_private.phone_no,
            "training": self.training.pk,
            "offer": self.offer.pk,
            "aeroclub_meber": self.client_private.aeroclub_meber,
            "company": self.company.pk,
        }
        response = self.client.post(
            reverse("clients_update", kwargs={"pk": self.client_private.pk}),
            data=update,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.client_private.refresh_from_db()
        self.assertEqual(self.client_private.name, update["name"])

    def test_view_client_update_changes_corporate_client_object_content(self):
        self.client.force_login(self.user)
        update = {
            "corporate_client": True,
            "company_name": "Test Company name",
            "nip": self.client_corporate.nip,
            "email": self.client_corporate.email,
            "phone_no": self.client_corporate.phone_no,
            "training": self.training.pk,
            "offer": self.offer.pk,
            "aeroclub_meber": self.client_corporate.aeroclub_meber,
            "company": self.company.pk,
        }
        response = self.client.post(
            reverse("clients_update", kwargs={"pk": self.client_corporate.pk}),
            data=update,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.client_corporate.refresh_from_db()
        self.assertEqual(self.client_corporate.company_name, update["company_name"])


class ClientsDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.client_private = ClientPrivateFactory.create(company=self.user.company)
        self.client_corporate = ClientCorporateFactory.create(company=self.user.company)

    def test_view_clients_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("clients_delete", kwargs={"pk": self.client_private.pk})
        )
        self.assertTemplateUsed(response, "clients/clients_delete.html")

    def test_view_buildings_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("clients_delete", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/clients/2/delete/")

    def test_clients_delete_view_deletes_client_private_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Client.objects.count(), 2)
        response = self.client.delete(
            reverse("clients_delete", kwargs={"pk": self.client_private.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Client.objects.count(), 1)

    def test_clients_delete_view_deletes_client_corporate_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Client.objects.count(), 2)
        response = self.client.delete(
            reverse("clients_delete", kwargs={"pk": self.client_corporate.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Client.objects.count(), 1)
