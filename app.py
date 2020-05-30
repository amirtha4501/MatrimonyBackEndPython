from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import DB_STRING
from session import SESSION

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from routes import ROUTES
for route in ROUTES:
    app.add_url_rule(route[1], view_func=route[2], methods=[route[0]])
