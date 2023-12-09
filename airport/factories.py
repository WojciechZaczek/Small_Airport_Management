from .models import Airport, Runway, Hangar, OutsideAircraftStand
from organization.factories import CompanyFactory
import factory


class AirportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Airport

    name = factory.Faker("word")
    city = factory.Faker("word")
    address = factory.Faker("sentence")
    contact = factory.Faker("word")
    types_of_traffic_permitted = factory.Faker(
        "random_element", elements=("VFR", "IFR")
    )
    radio = factory.Faker("pyfloat", positive=True)
    elevation = factory.Faker("pyint")
    co_ordinates = factory.Faker("word")
    description = factory.Faker("sentence")
    length = factory.Faker("pyint")
    width = factory.Faker("pyint")
    square_meters = factory.Faker("pyint")
    AIP = factory.django.FileField(filename="test_api.pdf", data=b"fake_binary_data")
    company = factory.SubFactory(CompanyFactory)


class RunwayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Runway

    name = factory.Faker("word")
    length = factory.Faker("pyfloat", positive=True)
    width = factory.Faker("pyfloat", positive=True)
    surface = factory.Faker("random_element", elements=("ASP", "GRS", "CON"))
    light = factory.Faker("boolean")
    markings = factory.Faker("boolean")
    TORA = factory.Faker("pyfloat", positive=True)
    LDA = factory.Faker("pyfloat", positive=True)
    CWY = factory.Faker("pyfloat", positive=True)
    SWY = factory.Faker("pyfloat", positive=True)
    airport = factory.SubFactory(AirportFactory)


class OutsideAircraftStandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OutsideAircraftStand

    name = factory.Faker("word")
    surface = factory.Faker("random_element", elements=("ASP", "GRS", "CON"))
    size = factory.Faker("random_element", elements=("S", "M", "L"))
    taken = factory.Faker("boolean")
    airport = factory.SubFactory(AirportFactory)


class HangarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hangar

    name = factory.Faker("word")
    hangar_height = factory.Faker("pyfloat", positive=True)
    hangar_wight = factory.Faker("pyfloat", positive=True)
    doors_height = factory.Faker("pyfloat", positive=True)
    doors_wight = factory.Faker("pyfloat", positive=True)
    small_stands_no = factory.Faker("pyint")
    small_stands_taken = factory.Faker("pyint")
    airport = factory.SubFactory(AirportFactory)
