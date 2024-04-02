from .models import Airport, Runway, Hangar, OutsideAircraftStand
from organization.factories import CompanyFactory
import factory
import factory.fuzzy


class AirportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Airport

    name = factory.fuzzy.FuzzyText(length=10)
    city = factory.fuzzy.FuzzyText(length=10)
    address = factory.Faker("sentence")
    contact = factory.fuzzy.FuzzyText(length=10)
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
    AIP = None  # factory.django.FileField(filename="test_api.pdf", data=b"fake_binary_data")
    company = factory.SubFactory(CompanyFactory)


class RunwayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Runway

    name = factory.fuzzy.FuzzyText(length=10)
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

    name = factory.fuzzy.FuzzyText(length=10)
    surface = factory.Faker("random_element", elements=("ASP", "GRS", "CON"))
    size = factory.Faker("random_element", elements=("S", "M", "L"))
    taken = factory.Faker("boolean")
    airport = factory.SubFactory(AirportFactory)


class HangarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hangar

    name = factory.fuzzy.FuzzyText(length=10)
    hangar_height = factory.Faker("pyfloat", positive=True)
    hangar_wight = factory.Faker("pyfloat", positive=True)
    doors_height = factory.Faker("pyfloat", positive=True)
    doors_wight = factory.Faker("pyfloat", positive=True)
    small_stands_no = 10
    small_stands_taken = 0
    airport = factory.SubFactory(AirportFactory)
