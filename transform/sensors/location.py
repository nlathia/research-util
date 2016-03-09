from sensor import Sensor


class Location(Sensor):

    TYPE = 'location'
    LOCATIONS = 'locations'
    PROVIDER = 'provider'
    UNKNOWN = 'unknown'
    TIME = 'time'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    CONTENT = [LATITUDE, LONGITUDE, 'bearing', PROVIDER, 'accuracy', 'speed', TIME]

    def __init__(self):
        pass

    @staticmethod
    def is_noise(sample):
        is_zero = sample[Location.LATITUDE] == 0 and sample[Location.LONGITUDE] == 0
        return sample[Location.PROVIDER] == Location.UNKNOWN or sample[Location.TIME] == 0 or is_zero

    def flatten(self, sample):
        user = [unicode(sample.get(u, '')).encode('UTF-8') for u in super(Location, self).header()]
        if Location.LOCATIONS in sample:
            for location in sample[Location.LOCATIONS]:
                if not Location.is_noise(location):
                    yield user + [unicode(location[c]).encode('UTF-8') for c in Location.CONTENT]
        elif not Location.is_noise(sample):
            yield user + [unicode(sample[c]).encode('UTF-8') for c in Location.CONTENT]

    def header(self):
        user = super(Location, self).header()
        return user + Location.CONTENT


class WiFiScan(Sensor):

    TYPE = 'wifi'
    RESULT = 'scanResult'
    CONTENT = ['ssid', 'bssid', 'level', 'frequency', 'capabilities']

    def __init__(self):
        pass

    def flatten(self, sample):
        user = [sample.get(u, None) for u in super(WiFiScan, self).header()]
        for result in sample.get(WiFiScan.RESULT, []):
            yield user + [unicode(result.get(r, '')).encode('UTF-8') for r in WiFiScan.CONTENT]

    def header(self):
        user = super(WiFiScan, self).header()
        return user + WiFiScan.CONTENT


