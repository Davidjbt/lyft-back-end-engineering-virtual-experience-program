from unittest import TestCase

from tyres.carrigan_tyres import CarriganTyres


class TestCarriganTyres(TestCase):

    def test_carrigan_tyres_should_be_serviced(self):
        sensors = [0, 1, 1, 1]
        tyres = CarriganTyres(sensors)

        self.assertTrue(tyres.needs_service())

    def test_carrigan_tyres_should_not_be_serviced(self):
        sensors = [0, 0, 0, 0]
        tyres = CarriganTyres(sensors)

        self.assertFalse(tyres.needs_service())
