class BasicFilter:

    @staticmethod
    def filter(*args, **kwargs):
        return True


class OneSchoolFilter(BasicFilter):

    @staticmethod
    def filter(current_user, target_user):
        return current_user.school == target_user.school
