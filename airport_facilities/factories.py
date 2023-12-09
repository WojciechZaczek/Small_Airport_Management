import factory
from .models import Building, Vehicle, Property, Others
from organization.factories import DepartmentFactory
from airport.factories import AirportFactory


class BuildingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Building

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    department = factory.SubFactory(DepartmentFactory)
    airport = factory.SubFactory(AirportFactory)


class VehicleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vehicle

    type = factory.Faker("word")
    registration_no = factory.Faker("word")
    description = factory.Faker("sentence")
    department = factory.SubFactory(DepartmentFactory)
    airport = factory.SubFactory(AirportFactory)


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    department = factory.SubFactory(DepartmentFactory)
    airport = factory.SubFactory(AirportFactory)


class OthersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Others

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    department = factory.SubFactory(DepartmentFactory)
    airport = factory.SubFactory(AirportFactory)
