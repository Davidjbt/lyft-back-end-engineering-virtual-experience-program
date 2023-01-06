from engine.engine import Engine

class SternmanEngine(Engine):

    def __init__(self, warning_light):
        self.warning_light = warning_light

    def needs_service(self):
        return self.warning_light