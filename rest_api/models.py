from flask.globals import g
from peewee import IntegerField, Model


class BaseModel(Model):
    id = IntegerField(primary_key=True)

    class Meta:
        database = g.db


class DateModel(BaseModel):
    year = IntegerField()
    month = IntegerField()
    day = IntegerField()


class DateTimeModel(DateModel):
    hours = IntegerField()
    minutes = IntegerField()

