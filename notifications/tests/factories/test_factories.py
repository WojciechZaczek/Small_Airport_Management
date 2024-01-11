from django.test import TestCase
from notifications.models import Notification
from notifications.factories import NotificationFactory
from users.models import CustomUser
from airport.models import Airport


class NotificationFactoriesTest(TestCase):
    def test_notification_factory_create_object(self):
        NotificationFactory.create()
        self.assertEqual(Notification.objects.count(), 1)

    def test_notification_factory_create_batch_objects(self):
        NotificationFactory.create_batch(
            10,
        )
        self.assertEqual(Notification.objects.count(), 10)

    def test_notification_factory_create_author_subfactory_object(self):
        NotificationFactory.create()
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_notification_factory_create_author_subfactory_object_batch_objects(self):
        NotificationFactory.create_batch(10)
        self.assertEqual(CustomUser.objects.count(), 10)

    def test_notification_factory_create_airport_subfactory_object(self):
        NotificationFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_notification_factory_create_airport_subfactory_object_batch_objects(self):
        NotificationFactory.create_batch(10)
        self.assertEqual(Airport.objects.count(), 10)
