from flask import Flask
from flask import render_template
from app import app, mongo, single_forms_file, forms_file
from werkzeug.exceptions import NotFound


@app.route('/')
def index():
    return "aaa"


@app.route('/<form_name>/<per_to>/<per_from>')
def fuck_off(form_name, per_to, per_from):
    if form_name in forms_file:
        return render_template(
            "base.html",
            content=forms_file[form_name].format(
                per_to=per_to,
                per_from=per_from)
        )
    else:
        raise NotFound()


@app.route('/<form_name>/<per_from>')
def fuck_off_single(form_name, per_from):
    if form_name in single_forms_file:
        return render_template(
            "base.html",
            content=single_forms_file[form_name].format(
            per_from=per_from)
        )
    else:
        raise NotFound()
