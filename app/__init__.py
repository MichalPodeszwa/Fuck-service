from flask import Flask
from pymongo import MongoClient
import json
from . import utils
from . import config

utils.config_init()

app = Flask(__name__)
db = MongoClient()

with open(config.DOUBLE_FORMS) as forms_file:
    forms_file = json.load(forms_file)
with open(config.SINGLE_FORMS) as single_forms_file:
    single_forms_file = json.load(single_forms_file)

from app import views
