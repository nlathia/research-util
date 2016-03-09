from activity import Accelerometer, StepCounter
from app import Interaction
from device import Battery
from contentreader import CallContentReader, SMSContentReader
from location import Location, WiFiScan

SENSOR_TYPE = 'dataType'

SENSORS = {
    Accelerometer.TYPE: Accelerometer(),
    Battery.TYPE: Battery(),
    CallContentReader.TYPE: CallContentReader(),
    SMSContentReader.TYPE: SMSContentReader(),
    Location.TYPE: Location(),
    WiFiScan.TYPE: WiFiScan(),
    StepCounter.TYPE: StepCounter(),
    Interaction.TYPE: Interaction()
}


def get_sensor(sensor_type):
    if sensor_type in SENSORS:
        return SENSORS[sensor_type]
    else:
        raise NotImplementedError('Unimplemented sensor: ' + str(sensor_type))


def get_sensor_from_sample(sample):
    sensor_type = sample[SENSOR_TYPE].lower()
    return get_sensor(sensor_type)





