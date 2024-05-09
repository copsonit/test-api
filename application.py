from flask import Flask
from flask_mongoengine import MongoEngine

from settings import MONGODB_HOST

db = MongoEngine()


from home.views import home_app
from pet.views import pet_app
from app.views import app_app

app = Flask(__name__)

app.config.from_pyfile('settings.py')

db.init_app(app)

app.register_blueprint(home_app)
app.register_blueprint(pet_app)
app.register_blueprint(app_app)