from flask import render_template
from app import app, single_forms_file, forms_file
from werkzeug.exceptions import NotFound


@app.route('/')
def index():
    return render_template(
        "index.html",
        singles=[form for form in single_forms_file],
        doubles=[form for form in forms_file]
    )


@app.route("/<form_name>/<person_to>/<person_from>")
@app.route("/<form_name>/<person_from>")
def give_a_fuck(form_name, person_from, person_to=None):
    if form_name in single_forms_file:
        content = single_forms_file[form_name].format(person_from=person_from)
    elif form_name in forms_file:
        content = forms_file[form_name].format(person_from=person_from, person_to=person_to)
    else:
        raise NotFound()
    return render_template(
        "output.html",
        content=content
    )


# @app.route('/<form_name>/<per_to>/<per_from>')
# @app.route('/<form_name>/<per_from>')
# def fuck_off(form_name, per_from, per_to=None):

#     if form_name not in forms_file:
#         if form_name not in single_forms_file:
#             return "NOPE"
#             raise NotFound()
#     if per_to:
#         return {"content": forms_file[form_name].format(
#             per_to=per_to,
#             per_from=per_from)
#         }
#     else:
#         return {"content": single_forms_file[form_name].format(
#                 per_from=per_from
#                 )
#         }
