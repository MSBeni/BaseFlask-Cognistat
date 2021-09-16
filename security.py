from werkzeug.security import safe_str_cmp
from model.user import User


def auth_(username, password):
    user = User.get_user_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    userID = payload['identity']
    return User.get_user_by_id(userID)
