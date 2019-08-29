from infolesson.utils import db_utils


class BasicPermission:

    def __init__(self, filters=None):
        if filters is None:
            self.filters = []
        else:
            self.filters = filters

    def check(self, **kwargs):
        for f in self.filters:
            if not f.filter(**kwargs):
                return False
        return True


class Role:

    def __init__(self, name, parent=None):
        self.name = name
        self.perms = []
        self.parent = parent

    def has_perm(self, perm, **kwargs):  # give class of permission to perm argument
        for p in self.perms:
            if isinstance(p, perm):
                return p.check(**kwargs)
        if self.parent is not None:
            return self.parent.has_perm(perm)
        return False


def login_required(func, *args, **kwargs):

    def wrapper():
        if db_utils.get_current_user() is None:
            return "Login required"
        return func(*args, **kwargs)

    return wrapper
