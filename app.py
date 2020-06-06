from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import DB_STRING
from session import SESSION

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app, session_options={'autocommit': True}, engine_options={'echo':True})

@app.errorhandler(400)
def custom400(error):
    return jsonify(error.description), 400

@app.after_request
def cors(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.set('Access-Control-Allow-Headers', '*')
    return response

from routes import ROUTES
for route in ROUTES:
    app.add_url_rule(route[1], view_func=route[2], methods=[route[0]])
