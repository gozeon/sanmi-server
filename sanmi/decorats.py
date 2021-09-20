from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify


def auth_role(role_list=[]):
    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            user = get_jwt_identity()
            if user.get('role').get('name') in role_list:
                return function(*args, **kwargs)
            else:
                return jsonify(msg="no auth")

        return wrapper

    return decorator
