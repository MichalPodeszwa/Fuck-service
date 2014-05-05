from flask import Flask
from flask import render_template, request, jsonify
from app import app, mongo, single_forms_file, forms_file
from werkzeug.exceptions import NotFound
import mimerender
import json


mimerender = mimerender.FlaskMimeRender()

render_xml = lambda content: '<content>{}</content>'.format(content)
render_json = lambda **args: jsonify(args)
render_html = lambda content: render_template('base.html', content=content)
render_txt = lambda content: content


@app.errorhandler(404)
@app.route('/')
def index(*args, **kwargs):
    return "Use proper URLs"



@app.route('/<form_name>/<per_to>/<per_from>')
@mimerender(
    default = "txt",
    html = render_html,
    xml  = render_xml,
    json = render_json,
    txt  = render_txt
)
def fuck_off(form_name, per_to, per_from):
    if form_name in forms_file:
        return {"content": forms_file[form_name].format(
            per_to=per_to,
            per_from=per_from)}
        return render_template(
            "base.html",
            content=forms_file[form_name].format(
                per_to=per_to,
                per_from=per_from)
        )
    else:
        raise NotFound()

@mimerender(
    default = 'html',
    html = render_html,
    xml  = render_xml,
    json = render_json,
    txt  = render_txt
)
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
