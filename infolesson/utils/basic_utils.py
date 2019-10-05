from flask import render_template


def get_current_user():
    return None  # TODO connection to DB


def render(template, **kwargs):
    return render_template(template, user=get_current_user(), **kwargs)
