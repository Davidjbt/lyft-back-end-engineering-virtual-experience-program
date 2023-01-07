from tyres.tyres import Tyres


class CarriganTyres(Tyres):

    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        # raise NotImplementedError
        for i in self.sensors:
            if i >= 0.9:
                return True
        return False
