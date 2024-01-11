from django.test import TestCase
from airport_facilities.models import Building, Others, Property, Vehicle
from airport_facilities.factories import (
    BuildingFactory,
    OthersFactory,
    PropertyFactory,
    VehicleFactory,
)
from airport.models import Airport
from organization.models import Department


class BuildingFactoriesTest(TestCase):
    def test_building_factory_create_object(self):
        BuildingFactory.create()
        self.assertEqual(Building.objects.count(), 1)

    def test_building_factory_create_batch_objects(self):
        BuildingFactory.create_batch(
            10,
        )
        self.assertEqual(Building.objects.count(), 10)

    def test_building_factory_create_airport_subfactory_object(self):
        BuildingFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_building_factory_create_department_subfactory_object(self):
        BuildingFactory.create()
        self.assertEqual(Department.objects.count(), 1)

    def test_building_factory_create_airport_subfactory_batch_objects(self):
        BuildingFactory.create_batch(
            10,
        )
        self.assertEqual(Airport.objects.count(), 10)

    def test_building_factory_create_department_subfactory_batch_objects(self):
        BuildingFactory.create_batch(
            10,
        )
        self.assertEqual(Department.objects.count(), 10)


class OthersFactoriesTest(TestCase):
    def test_others_factory_create_object(self):
        OthersFactory.create()
        self.assertEqual(Others.objects.count(), 1)

    def test_others_factory_create_batch_objects(self):
        OthersFactory.create_batch(10)
        self.assertEqual(Others.objects.count(), 10)

    def test_others_factory_create_airport_subfactory_object(self):
        OthersFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_others_factory_create_department_subfactory_object(self):
        OthersFactory.create()
        self.assertEqual(Department.objects.count(), 1)

    def test_others_factory_create_airport_subfactory_batch_objects(self):
        OthersFactory.create_batch(
            10,
        )
        self.assertEqual(Airport.objects.count(), 10)

    def test_others_factory_create_department_subfactory_batch_objects(self):
        OthersFactory.create_batch(
            10,
        )
        self.assertEqual(Department.objects.count(), 10)


class PropertyFactoriesTest(TestCase):
    def test_property_factory_create_object(self):
        PropertyFactory.create()
        self.assertEqual(Property.objects.count(), 1)

    def test_property_factory_create_batch_objects(self):
        PropertyFactory.create_batch(10)
        self.assertEqual(Property.objects.count(), 10)

    def test_property_factory_create_airport_subfactory_object(self):
        PropertyFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_property_factory_create_department_subfactory_object(self):
        PropertyFactory.create()
        self.assertEqual(Department.objects.count(), 1)

    def test_property_factory_create_airport_subfactory_batch_objects(self):
        PropertyFactory.create_batch(
            10,
        )
        self.assertEqual(Airport.objects.count(), 10)

    def test_property_factory_create_department_subfactory_batch_objects(self):
        PropertyFactory.create_batch(
            10,
        )
        self.assertEqual(Department.objects.count(), 10)


class VehicleFactoriesTest(TestCase):
    def test_vehicle_factory_create_object(self):
        VehicleFactory.create()
        self.assertEqual(Vehicle.objects.count(), 1)

    def test_vehicle_factory_create_batch_objects(self):
        VehicleFactory.create_batch(10)
        self.assertEqual(Vehicle.objects.count(), 10)

    def test_vehicle_factory_create_airport_subfactory_object(self):
        VehicleFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_vehicle_factory_create_department_subfactory_object(self):
        VehicleFactory.create()
        self.assertEqual(Department.objects.count(), 1)

    def test_vehicle_factory_create_airport_subfactory_batch_objects(self):
        VehicleFactory.create_batch(
            10,
        )
        self.assertEqual(Airport.objects.count(), 10)

    def test_vehicle_factory_create_department_subfactory_batch_objects(self):
        VehicleFactory.create_batch(
            10,
        )
        self.assertEqual(Department.objects.count(), 10)
