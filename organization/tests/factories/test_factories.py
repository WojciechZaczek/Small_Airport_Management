from django.test import TestCase
from organization.models import Company, Department, Worker
from organization.factories import CompanyFactory, DepartmentFactory, WorkerFactory


class CompanyFactoriesTest(TestCase):
    def test_company_factory_create_object(self):
        CompanyFactory.create()
        self.assertEqual(Company.objects.count(), 1)

    def test_company_factory_create_batch_objects(self):
        CompanyFactory.create_batch(
            10,
        )
        self.assertEqual(Company.objects.count(), 10)


class DepartmentFactoriesTest(TestCase):
    def test_department_factory_create_object(self):
        DepartmentFactory.create()
        self.assertEqual(Department.objects.count(), 1)

    def test_department_factory_create_batch_objects(self):
        DepartmentFactory.create_batch(
            10,
        )
        self.assertEqual(Department.objects.count(), 10)

    def test_department_factory_create_company_subfactory_object(self):
        DepartmentFactory.create()
        self.assertEqual(Company.objects.count(), 1)

    def test_department_factory_create_company_subfactory_batch_objects(self):
        DepartmentFactory.create_batch(
            10,
        )
        self.assertEqual(Company.objects.count(), 10)


class WorkerFactoriesTest(TestCase):
    def test_worker_factory_create_object(self):
        WorkerFactory.create()
        self.assertEqual(Worker.objects.count(), 1)

    def test_worker_factory_create_batch_objects(self):
        WorkerFactory.create_batch(
            10,
        )
        self.assertEqual(Worker.objects.count(), 10)

    def test_worker_factory_create_company_subfactory_object(self):
        WorkerFactory.create()
        self.assertEqual(Company.objects.count(), 1)

    def test_worker_factory_create_company_subfactory_batch_objects(self):
        WorkerFactory.create_batch(
            10,
        )
        self.assertEqual(Company.objects.count(), 10)
