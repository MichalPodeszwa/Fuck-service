from flask import Flask
from pymongo import MongoClient
import json

app = Flask(__name__)

with open('app/static/forms.json') as forms_file:
    forms_file = json.load(forms_file)
with open('app/static/single_forms.json') as single_forms_file:
    single_forms_file = json.load(single_forms_file)

from app import views
