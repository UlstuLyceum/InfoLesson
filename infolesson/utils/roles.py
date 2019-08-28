from infolesson.utils.perms_control import Role
from infolesson.utils.filters import OneSchoolFilter
from infolesson.modules.auth.perms import *


student_role = Role('student')
student_role.perms.append(ProfileAccess(filters=[
    OneSchoolFilter
]))
