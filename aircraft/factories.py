from .models import Aircraft, AircraftHangared
import factory
import factory.fuzzy
from airport.factories import HangarFactory, OutsideAircraftStandFactory
from clients.factories import ClientPrivateFactory, ClientCorporateFactory


class AircraftFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Aircraft

    manufacture = factory.fuzzy.FuzzyText(length=10)
    name = factory.fuzzy.FuzzyText(length=10)
    type = factory.Faker(
        "random_element", elements=("A", "H", "AS", "G", "P", "B", "UAV")
    )
    take_off_ground = factory.Faker("pyint")
    take_off_over_50ft_distance = factory.Faker("pyint")
    landing_groundroll = factory.Faker("pyint")
    fuel_capacity = factory.Faker("pyint")
    runway_surface_type = factory.Faker(
        "random_element", elements=("GRS", "CON", "ASPH")
    )
    description = factory.Faker("sentence")


class AircraftHangaredFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AircraftHangared

    aircraft = factory.SubFactory(AircraftFactory)
    aircraft_registration_no = factory.fuzzy.FuzzyText(length=10)
    airport_property = factory.Faker("boolean")
    hangar = factory.SubFactory(HangarFactory)
    outside_stand = factory.SubFactory(OutsideAircraftStandFactory)
    client = factory.SubFactory(ClientPrivateFactory)
