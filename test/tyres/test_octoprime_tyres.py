from unittest import TestCase

from tyres.octoprime_tyres import OctoprimeTyres


class TestOctoprimeTyres(TestCase):

    def test_octoprime_tyres_should_be_serviced(self):
        sensors = [1, 1, 1, 0]
        tyres = OctoprimeTyres(sensors)

        self.assertTrue(tyres.needs_service())

    def test_octoprime_tyres_should_not_be_serviced(self):
        sensors = [1, 1, 0, 0]
        tyres = OctoprimeTyres(sensors)

        self.assertFalse(tyres.needs_service())
