from flask import Flask
from flask.ext.pymongo import PyMongo
import json

app = Flask(__name__)
app.config.from_object('config')

with open('app/static/forms.txt') as forms_file:
    forms_file = json.load(forms_file)
with open('app/static/single_forms.txt') as single_forms_file:
    single_forms_file = json.load(single_forms_file)

mongo = PyMongo(app, config_prefix='MONGO')
from app import views
