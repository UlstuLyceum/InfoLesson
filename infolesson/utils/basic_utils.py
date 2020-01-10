from flask import render_template
from flask_security import current_user


def get_current_user():  # TODO remove, useless function
    return current_user


def render(template, **kwargs):
    return render_template(template, user=get_current_user(), **kwargs)


def raise_error(error='Неизвестная ошибка'):
    return render('error.html', error=error)


def access_error():
    return raise_error('У вас нет доступа к этому разделу')


def teacher_role_or_more(user):
    return user.has_role("teacher") or user.has_role("headteacher") or user.has_role("admin")
