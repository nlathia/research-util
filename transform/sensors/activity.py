from sensor import Sensor


class Accelerometer(Sensor):

    TYPE = 'accelerometer'
    TIME_STAMPS = 'sensorTimeStamps'
    X_AXIS = 'xAxis'
    Y_AXIS = 'yAxis'
    Z_AXIS = 'zAxis'
    COLUMNS = ['time', X_AXIS, Y_AXIS, Z_AXIS]

    def __init__(self):
        pass

    def flatten(self, sample):
        user = [sample.get(u, None) for u in super(Accelerometer, self).header()]
        xs = sample.get(Accelerometer.X_AXIS, [])
        ys = sample.get(Accelerometer.Y_AXIS, [])
        zs = sample.get(Accelerometer.Z_AXIS, [])
        ts = sample.get(Accelerometer.TIME_STAMPS, [])
        min_length = min([len(xs), len(ys), len(zs), len(ts)])
        for i in xrange(0, min_length):
            yield user + [ts[i], xs[i], ys[i], zs[i]]

    def header(self):
        user = super(Accelerometer, self).header()
        return user + Accelerometer.COLUMNS


class StepCounter(Sensor):

    TYPE = 'stepcounter'
    CONTENT = ['lastBoot', 'lastBootMillis', 'stepCount']

    def __init__(self):
        pass

    def flatten(self, sample):
        yield [sample.get(u, None) for u in self.header()]

    def header(self):
        user = super(StepCounter, self).header()
        return user + StepCounter.CONTENT





