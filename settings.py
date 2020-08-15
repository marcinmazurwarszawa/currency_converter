from flask import Flask
from flask_sqlalchemy import SQLAlchemy


DB_PATH = 'sqlite:///currencies.db'

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH

db = SQLAlchemy(app)

RETURN_PRECISION = 4
NBP_BASE_CURRENCY_URL = 'http://api.nbp.pl/api/exchangerates/rates/A/'
