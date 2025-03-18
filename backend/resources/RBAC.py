from functools import wraps
from flask_jwt_extended import jwt_required,get_jwt
from flask import jsonify

def access_allowed(*required_roles):
        def wrapper(fn):
            @wraps(fn)
            @jwt_required()
            def decorator(*args,**kwargs):
                claims=get_jwt()
                role=claims.get('role')

                if role in required_roles:
                    return fn(*args,**kwargs)
                
                return jsonify (msg="You dont't have access to this route"),403
            return decorator
        return wrapper