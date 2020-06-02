from flask import Flask
from logging import info
from sqlalchemy_utils import create_database, database_exists

from config import Config
from populate_data import get_users, get_goods, get_stores
from database import db, User, Good, Store


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        if database_exists(db.engine.url):
            db.create_all()
            info(f'Database \'{Config.DB_NAME}\' exists')
        else:
            info(f"Database does not exists {db.engine.url}")
            create_database(db.engine.url)
            db.create_all()
            info(f'Database \'{Config.DB_NAME}\' created')

    fill_db(app, get_users, User)
    fill_db(app, get_goods, Good)
    fill_db(app, get_stores, Store)

    return app


def fill_db(app, func_for_fill, model):
    with app.app_context():
        elements = func_for_fill()
        for element in elements:
            db.session.add(model(**element))
        db.session.commit()
        info(f'{model.__name__} fill in DB successfully')


if __name__ == "__main__":
    app = create_app()
    app.run()