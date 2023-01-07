from datetime import datetime

from battery.battery import Battery

class SpindlerBattery(Battery):

    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        # Now the battery requires service 3 years instead 2
        return self.current_date > service_threshold_date
