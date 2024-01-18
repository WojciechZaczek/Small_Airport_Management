from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from organization.factories import CompanyFactory, DepartmentFactory
from airport.factories import AirportFactory


class CompanyViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create(name="Test company")
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.company)

    def test_view_company_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("organizations"))
        self.assertTemplateUsed(response, "organization/organization.html")

    def test_view_company_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("organizations"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/organizations/")

    def test_view_company_returns_correct_offer_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("organizations"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test company")

    def test_company_view_displayed_offer_price(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("organizations"))
        self.assertContains(response, self.department.name)


class CompanyUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
        self.airport = AirportFactory.create(company=self.user.company)

    def test_view_company_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("company_update", kwargs={"pk": self.company.pk})
        )
        self.assertTemplateUsed(response, "organization/company_form.html")

    def test_view_company_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("company_update", kwargs={"pk": self.company.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "/login/?next=/organizations/companies/1/update/"
        )
