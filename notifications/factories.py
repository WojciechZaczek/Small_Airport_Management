import factory.fuzzy
from .models import Notification
from airport.factories import AirportFactory
from users.factories import UserFactory


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    title = factory.Faker("word")
    content = factory.Faker("sentence")
    date_posted = factory.Faker("date_this_decade")
    author = factory.SubFactory(UserFactory)
    view_date = factory.Faker("date_this_decade")
    airport = factory.SubFactory(AirportFactory)
