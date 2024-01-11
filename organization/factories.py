from .models import Company, Department, Worker
import factory


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker("word")
    address = factory.Faker("sentence")
    telephone = factory.Faker("sentence")
    email_domain = factory.Faker("word")
    description = factory.Faker("sentence")


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    company = factory.SubFactory(CompanyFactory)


class WorkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Worker

    first_name = factory.Faker("word")
    last_name = factory.Faker("word")
    department = factory.Faker(
        "random_element",
        elements=("office", "control", "mechanic", "cleaning", "air", "IT", "external"),
    )
    job_position = factory.Faker(
        "random_element",
        elements=("ceo", "manager", "worker", "specialist", "pilot", "none", "admin"),
    )
    address = factory.Faker("sentence")
    phone_no = factory.Faker("sentence")
    information = factory.Faker("sentence")
    company = factory.SubFactory(CompanyFactory)
