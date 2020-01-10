from flask import render_template
from flask_security import current_user


def get_current_user():  # TODO remove, useless function
    return current_user


def render(template, **kwargs):
    return render_template(template, user=get_current_user(), **kwargs)
