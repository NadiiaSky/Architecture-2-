from rest_api.models import DateModel, DateTimeModel


class DateView:
    @staticmethod
    def generate_response(model: DateModel):
        return f'{model.year}.{model.month}.{model.day}'


class DateTimeView:
    @staticmethod
    def generate_response(model: DateTimeModel):
        return f'{model.year}.{model.month}.{model.day} {model.hours}:{model.minutes}'
