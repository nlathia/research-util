from sensor import Sensor


class Interaction(Sensor):

    TYPE = 'interaction'
    CATEGORY = 'category'
    ACTION = 'action'
    APP_USAGE = 'app_usage'
    SURVEY = 'survey'
    SYSTEM = 'system'
    NOTIFICATION = 'notification'
    COLUMNS = [CATEGORY, ACTION]

    def __init__(self):
        pass

    def flatten(self, sample):
        user = [sample.get(u, None) for u in super(Interaction, self).header()]
        row = user + [sample.get(u, None) for u in Interaction.COLUMNS]
        if sample[Interaction.CATEGORY] == Interaction.APP_USAGE:
            yield row + [sample.get('screen', None)]
        elif sample[Interaction.CATEGORY] == Interaction.NOTIFICATION:
            yield row + [sample.get('notification_id', None)]
        elif sample[Interaction.CATEGORY] == Interaction.SURVEY:
            yield row + [sample.get('survey_id', None)]
        elif sample[Interaction.CATEGORY] == Interaction.SYSTEM:
            yield row
        else:
            raise Exception('Unknown interaction category: '+sample[Interaction.CATEGORY])

    def header(self):
        user = super(Interaction, self).header()
        return user + Interaction.COLUMNS + ['detail']


