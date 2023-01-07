from tyres.tyres import Tyres


class OctoprimeTyres(Tyres):

    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        # raise NotImplementedError
        return sum(self.sensors) >= 3
