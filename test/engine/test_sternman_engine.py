from unittest import TestCase

from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(TestCase):

    def test_capulet_engine_should_be_serviced(self):
        warning_light = True

        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        warning_light = False

        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())
