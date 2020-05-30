from flask.globals import g
from peewee import IntegerField, Model

from model.models import Date, DateTime


class BaseModel(Model):
    id = IntegerField(primary_key=True)

    class Meta:
        database = g.db


class DateModel(BaseModel):
    validator = Date

    year = IntegerField()
    month = IntegerField()
    day = IntegerField()

    @classmethod
    def validate(cls, data):
        cls.validator(**data)


class DateTimeModel(DateModel):
    validator = DateTime

    hours = IntegerField()
    minutes = IntegerField()

