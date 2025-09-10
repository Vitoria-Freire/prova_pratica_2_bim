from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
csrf = CSRFProtect(app)

db.init_app(app)

from app import routes, models

with app.app_context():
    db.create_all()