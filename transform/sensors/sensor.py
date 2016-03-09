from abc import ABCMeta, abstractmethod


class Sensor:

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def flatten(self, sample):
        pass

    @abstractmethod
    def header(self):
        return ['userid', 'deviceid', 'senseStartTime', 'senseStartTimeMillis']

