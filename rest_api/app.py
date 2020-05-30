from flask import Flask
from peewee import SqliteDatabase

from rest_api.data_source import init_db

# settings
DEBUG = True
DATABASE_URL = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config.from_object('rest_api.app')

    with app.app_context():
        # dependency injection
        database = SqliteDatabase(app.config['DATABASE_URL'])
        init_db(database)

    from rest_api.urls import datetime_bp
    app.register_blueprint(datetime_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
