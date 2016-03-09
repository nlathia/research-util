from math import sqrt

import numpy as np


class Accelerometer(object):

    X = 'xAxis'
    Y = 'yAxis'
    Z = 'zAxis'
    # TIME_STAMPS = 'sensorTimeStamps'
    USER = 'userid'
    TIME = 'senseStartTime'

    def __init__(self, sample):
        self.user = sample[Accelerometer.USER]
        self.time = sample[Accelerometer.TIME]
        self.xs = [float(sample[Accelerometer.X][i]) for i in xrange(0, len(sample[Accelerometer.X]))]
        self.ys = [float(sample[Accelerometer.Y][i]) for i in xrange(0, len(sample[Accelerometer.Y]))]
        self.zs = [float(sample[Accelerometer.Z][i]) for i in xrange(0, len(sample[Accelerometer.Z]))]
        self.min_size = min(len(self.xs), len(self.ys), len(self.zs))
        self.xs = self.xs[:self.min_size]
        self.ys = self.ys[:self.min_size]
        self.zs = self.zs[:self.min_size]

    @staticmethod
    def features_header():
        return [Accelerometer.USER, Accelerometer.TIME, 'magnitude_sd']

    def magnitude_std(self):
        magnitude = []
        for i in xrange(0, self.min_size):
            x2 = self.xs[i] * self.xs[i]
            y2 = self.ys[i] * self.ys[i]
            z2 = self.zs[i] * self.zs[i]
            magnitude.append(sqrt(x2 + y2 + z2))
        return np.std(magnitude)

    def get_features(self):
        return [self.user, self.time, self.magnitude_std()]





