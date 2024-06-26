import factory.fuzzy
from .models import Offer, Training
from airport.factories import AirportFactory
from organization.factories import WorkerFactory


class OfferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offer

    name = factory.fuzzy.FuzzyText(length=10)
    price = factory.Faker("pyfloat")
    description = factory.Faker("sentence")
    airport = factory.SubFactory(AirportFactory)


class TrainingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Training

    name = factory.fuzzy.FuzzyText(length=10)
    price = factory.Faker("pyfloat")
    description = factory.Faker("sentence")
    hours = factory.Faker("pyint")
    worker = factory.SubFactory(WorkerFactory)
    airport = factory.SubFactory(AirportFactory)
