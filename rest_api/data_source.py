from flask import g


def init_db(db_engine):
    db = get_db(db_engine)

    from rest_api.models import DateModel, DateTimeModel
    db.create_tables([DateModel, DateTimeModel])


def get_db(db_engine):
    if 'db' not in g:
        g.db = connect_to_database(db_engine)
    return g.db


def connect_to_database(db_engine):
    db_engine.connect()
    return db_engine
