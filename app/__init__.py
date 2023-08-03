from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
from flask_migrate import Migrate

ENV_VARIABLES = dotenv_values(".env")


app = Flask(__name__)
app.config.from_object(ENV_VARIABLES["SERVER_CONFIGURATION"])


db = SQLAlchemy()
db.init_app(app)


migrate = Migrate(app, db, compare_type=True)
