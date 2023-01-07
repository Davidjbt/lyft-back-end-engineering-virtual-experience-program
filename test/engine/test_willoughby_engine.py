from unittest import TestCase

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(TestCase):

    def test_willoughby_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60001

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60000

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
