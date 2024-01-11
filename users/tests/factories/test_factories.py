from django.test import TestCase
from users.models import CustomUser
from users.factories import UserFactory
from organization.models import Company


class UserFactoriesTest(TestCase):
    def test_user_factory_create_object(self):
        UserFactory.create()
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_user_factory_create_batch_objects(self):
        UserFactory.create_batch(
            10,
        )
        self.assertEqual(CustomUser.objects.count(), 10)

    def test_user_factory_create_company_subfactory_object(self):
        UserFactory.create()
        self.assertEqual(Company.objects.count(), 1)

    def test_user_factory_create_company_subfactory_batch_objects(self):
        UserFactory.create_batch(
            10,
        )
        self.assertEqual(Company.objects.count(), 10)
