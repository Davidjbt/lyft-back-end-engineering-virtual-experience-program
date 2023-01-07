from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car
from tyres.carrigan_tyres import CarriganTyres
from tyres.octoprime_tyres import OctoprimeTyres


class CarFactor:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tyres = OctoprimeTyres(sensors)
        return Car(engine, battery, tyres)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tyres = CarriganTyres(sensors)
        return Car(engine, battery, tyres)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light, sensors):
        engine = SternmanEngine(warning_light)
        battery = SpindlerBattery(last_service_date, current_date)
        tyres = OctoprimeTyres(sensors)
        return Car(engine, battery, tyres)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tyres = CarriganTyres(sensors)
        return Car(engine, battery, tyres)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tyres = OctoprimeTyres(sensors)
        return Car(engine, battery, tyres)
