import unittest
from sensor import EntrySensor, ExitSensor, Sensor
from car_park import CarPark

class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.entrySensor = EntrySensor(
            id = "12345",
            car_park = CarPark("123 Example Street", 100),
            is_active = True
        )

    def test_EntrySensor_init_method(self):
        self.assertIsInstance(self.entrySensor, Sensor)
        self.assertIsInstance(self.entrySensor, EntrySensor)
        self.assertIsInstance(self.entrySensor.car_park, CarPark)
        self.assertEqual(self.entrySensor.id, "12345")
        self.assertEqual(self.entrySensor.is_active, True)



class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.exitSensor = ExitSensor(
            id = "54321",
            car_park = CarPark("123 Example Street", 100)
        )

    def test_ExitSensor_init_method(self):
        self.assertIsInstance(self.exitSensor, Sensor)
        self.assertIsInstance(self.exitSensor, ExitSensor)
        self.assertIsInstance(self.exitSensor.car_park, CarPark)
        self.assertEqual(self.exitSensor.id, "54321")
        self.assertEqual(self.exitSensor.is_active, False)