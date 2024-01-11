import factory
from .models import Client
from organization.factories import CompanyFactory
from offer.factories import TrainingFactory, OfferFactory


class ClientCorporateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    corporate_client = True
    name = None
    last_name = None
    pesel = None
    company_name = factory.Faker("company")
    nip = factory.Faker("pyint")
    email = factory.Faker("name")
    phone_no = factory.Faker("pyint")

    training = factory.RelatedFactory(TrainingFactory)
    offer = factory.RelatedFactory(OfferFactory)
    aeroclub_meber = factory.Faker("boolean")
    company = factory.SubFactory(CompanyFactory)


class ClientPrivateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    corporate_client = False
    name = factory.Faker("name")
    last_name = factory.Faker("last_name")
    pesel = factory.Faker("pyint")
    company_name = None
    nip = None
    email = factory.Faker("name")
    phone_no = factory.Faker("pyint")

    training = factory.RelatedFactory(TrainingFactory)
    offer = factory.RelatedFactory(OfferFactory)
    aeroclub_meber = factory.Faker("boolean")
    company = factory.SubFactory(CompanyFactory)
