from datetime import datetime
from unittest import TestCase

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(TestCase):

    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today()
        last_service_date = datetime.today().replace(year=current_date.year - 5)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        current_date = datetime.today()
        last_service_date = datetime.today().replace(year=current_date.year - 1)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
