from .models import Company, Department, Worker
import factory.fuzzy


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.fuzzy.FuzzyText(length=10)
    address = factory.Faker("sentence")
    telephone = factory.Faker("sentence")
    email_domain = factory.fuzzy.FuzzyText(length=10)
    description = factory.Faker("sentence")


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    name = factory.fuzzy.FuzzyText(length=10)
    description = factory.Faker("sentence")
    company = factory.SubFactory(CompanyFactory)


class WorkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Worker

    first_name = factory.fuzzy.FuzzyText(length=10)
    last_name = factory.fuzzy.FuzzyText(length=10)
    department = factory.Faker(
        "random_element",
        elements=("office", "control", "mechanic", "cleaning", "air", "IT", "external"),
    )
    job_position = factory.Faker(
        "random_element",
        elements=("ceo", "manager", "worker", "specialist", "pilot", "none", "admin"),
    )
    address = factory.Faker("sentence")
    phone_no = factory.fuzzy.FuzzyText(length=10)
    information = factory.fuzzy.FuzzyText(length=10)
    company = factory.SubFactory(CompanyFactory)
