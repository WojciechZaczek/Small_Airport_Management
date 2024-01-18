from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from clients.factories import ClientPrivateFactory, ClientCorporateFactory


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/clients/")

    def test_view_clients_returns_correct_private_client_last_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testowy")

    def test_view_clients_returns_correct_corporate_client_last_company_name_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Company")

    def test_view_clients_returns_correct_private_client_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.client_private.name)

    def test_view_clients_returns_correct_corporate_client_nip_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual(response.status_code, 302)
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
        self.assertEqual(response.status_code, 302)
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/clients/new/")


class ClientsCorporateCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.client_corporate = ClientCorporateFactory.create(
            company=self.user.company,
        )

    def test_view_client_corporate_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients_add_corporate"))
        self.assertTemplateUsed(response, "clients/clients_corporate_form.html")

    def test_view_client_corporate_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("clients_add_corporate"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/clients/new/corporate/")


class ClientsPrivateCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.client_private = ClientPrivateFactory.create(
            company=self.user.company,
        )

    def test_view_client_corporate_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("clients_add_private"))
        self.assertTemplateUsed(response, "clients/clients_private_form.html")

    def test_view_client_corporate_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("clients_add_private"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/clients/new/private/")


class ClientsUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/clients/1/update/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/clients/2/delete/")
