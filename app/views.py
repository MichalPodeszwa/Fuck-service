from flask import Flask
from flask import render_template, request, jsonify, flash, redirect
from app import app, mongo, single_forms_file, forms_file
from werkzeug.exceptions import NotFound
import mimerender
import json
from bson.objectid import ObjectId

mimerender = mimerender.FlaskMimeRender()

render_xml = lambda content: '<content>{}</content>'.format(content)
render_json = lambda **args: jsonify(args)
render_html = lambda content: render_template('base.html', content=content)
render_txt = lambda content: content


@app.errorhandler(404)
def error(*args, **kwargs):
    flash("Use proper URLs")
    return redirect('/')


@app.route('/')
def index(*args, **kwargs):
    return render_template("index.html")


@app.route('/stats')
def stats():
    froms = mongo.db.stats.froms.find({})
    tos = mongo.db.stats.tos.find({})
    return render_template("stats.html",
                           froms=froms,
                           tos=tos)


def increment(username, user_from):
    if user_from:
        stat = mongo.db.stats.froms.find_one({"name": username})
    else:
        stat = mongo.db.stats.tos.find_one({"name": username})
    if stat:
        stat["amount"] += 1
        if user_from:
            mongo.db.stats.froms.update({"_id": ObjectId(stat["_id"])}, stat)
        else:
            mongo.db.stats.tos.update({"_id": ObjectId(stat["_id"])}, stat)
    else:
        if user_from:
            mongo.db.stats.froms.insert({"name": username, "amount": 1})
        else:
            mongo.db.stats.tos.insert({"name": username, "amount": 1})


@app.route('/<form_name>/<per_to>/<per_from>')
@app.route('/<form_name>/<per_from>')
@mimerender(
    default="txt",
    html=render_html,
    xml=render_xml,
    json=render_json,
    txt=render_txt
)
def fuck_off(form_name, per_from, per_to=None):
    increment(per_from, True)
    if per_to:
        increment(per_to, False)

    if form_name not in forms_file:
        if form_name not in single_forms_file:
            return "NOPE"
            raise NotFound()
    if per_to:
        return {"content": forms_file[form_name].format(
            per_to=per_to,
            per_from=per_from)
        }
    else:
        return {"content": single_forms_file[form_name].format(
                per_from=per_from
            )
        }