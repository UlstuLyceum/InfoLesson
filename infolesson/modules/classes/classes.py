from flask import Blueprint
from flask_login import current_user
from flask_security import roles_accepted

from infolesson.utils.basic_utils import raise_error, access_error, teacher_role_or_more, render
from infolesson.utils.models import School

classes = Blueprint("classes", __name__, template_folder="templates")


@classes.route('/school/<int:school_id>/classes')
@roles_accepted("teacher", "headteacher", "admin")
def school_classes_page(school_id):
    school = School.query.filter(School.id == school_id).first()
    if school is None:
        return raise_error("Такой школы не существует")
    if school_id != current_user.school.id and not current_user.has_role("admin"):
        return access_error()
    return render('classes-list.html', school=school)

@classes.route('/123')
@roles_accepted("123")
def one_tow():
    return 'ok'
