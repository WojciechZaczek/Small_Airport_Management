import factory
import factory.fuzzy
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
    company_name = factory.fuzzy.FuzzyText(length=10)
    nip = factory.Faker("pyint")
    email = factory.fuzzy.FuzzyText(length=10)
    phone_no = factory.Faker("pyint")

    training = factory.RelatedFactory(TrainingFactory)
    offer = factory.RelatedFactory(OfferFactory)
    aeroclub_meber = factory.Faker("boolean")
    company = factory.SubFactory(CompanyFactory)


class ClientPrivateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    corporate_client = False
    name = factory.fuzzy.FuzzyText(length=10)
    last_name = factory.fuzzy.FuzzyText(length=10)
    pesel = factory.Faker("pyint")

    email = factory.fuzzy.FuzzyText(length=10)
    phone_no = factory.Faker("pyint")

    training = factory.RelatedFactory(TrainingFactory)
    offer = factory.RelatedFactory(OfferFactory)
    aeroclub_meber = factory.Faker("boolean")
    company = factory.SubFactory(CompanyFactory)
