import factory
from .models import CustomUser
from organization.factories import CompanyFactory
from django.contrib.auth.models import Group


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker("word")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: f"user{n}")
    password = factory.Faker("word")
    first_name = factory.Faker("word")
    last_name = factory.Faker("word")
    email = factory.Faker("word")

    department = factory.Faker(
        "random_element",
        elements=("office", "control", "mechanic", "cleaning", "air", "IT", "external"),
    )
    job_position = factory.Faker(
        "random_element",
        elements=("ceo", "manager", "worker", "specialist", "pilot", "admin"),
    )
    company = factory.SubFactory(CompanyFactory)

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.groups.add(*extracted)
        else:
            group = GroupFactory.create()
            self.groups.add(group)
