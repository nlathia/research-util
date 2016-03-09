from sensor import Sensor
from abc import ABCMeta

CONTENT_LIST = 'contentList'


class ContentReader(Sensor):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def flatten(self, sample, columns):
        user = [sample.get(u, None) for u in super(ContentReader, self).header()]
        for entry in sample.get(CONTENT_LIST, []):
            content = [entry.get(c, None) for c in columns]
            yield user + content

    def header(self):
        return super(ContentReader, self).header()


class CallContentReader(ContentReader):

    TYPE = 'callcontentreader'
    CONTENT = ['number', 'type', 'duration', 'date', 'local_time_when_sensed']

    def __init__(self):
        pass

    def flatten(self, sample):
        for result in super(CallContentReader, self).flatten(sample, CallContentReader.CONTENT):
            yield result

    def header(self):
        user = super(CallContentReader, self).header()
        return user + CallContentReader.CONTENT


class SMSContentReader(ContentReader):

    TYPE = 'smscontentreader'
    CONTENT = ['address', 'type', 'bodyWordCount', 'bodyLength', 'date', 'local_time_when_sensed']

    def __init__(self):
        pass

    def flatten(self, sample):
        for result in super(SMSContentReader, self).flatten(sample, SMSContentReader.CONTENT):
            yield result

    def header(self):
        user = super(SMSContentReader, self).header()
        return user + SMSContentReader.CONTENT


