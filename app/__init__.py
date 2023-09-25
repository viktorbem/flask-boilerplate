import os

from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient

from app.blueprints.pages import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # MongoDB connection
    app.config['MONGODB_URI'] = os.environ.get('MONGODB_URI')
    app.db = MongoClient(app.config['MONGODB_URI']).get_default_database()

    # Blueprints
    app.register_blueprint(pages)

    return app
