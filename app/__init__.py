from flask import Flask
import json
from sqlalchemy import create_engine
from . import utils, config
from .models import DBSession, Base

utils.config_init()

app = Flask(__name__)
engine = create_engine(config.DB_URL)
DBSession.configure(bind=engine)
Base.metadata.bind = engine

with open(config.DOUBLE_FORMS) as forms_file:
    forms_file = json.load(forms_file)
with open(config.SINGLE_FORMS) as single_forms_file:
    single_forms_file = json.load(single_forms_file)

from app import views
