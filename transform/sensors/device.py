from sensor import Sensor


class Battery(Sensor):

    TYPE = 'battery'

    def __init__(self):
        pass

    def flatten(self, sample):
        yield [sample.get(u, None) for u in self.header()]

    def header(self):
        user = super(Battery, self).header()
        return user + ['status', 'temperature', 'level', 'scale', 'plugged', 'voltage', 'health']




