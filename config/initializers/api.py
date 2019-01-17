from .flask import app
from flask_restful import Api
import functools
api = Api()

def resources(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        func(*args, **kw)
        api.init_app(app)
    return wrapper


# def resources(func):
#     @functools.wraps(func)
#     def wrapper(api):
#         print('call %s():' % func.__name__)
#         func(api)
#         api.init_app(app)
#     return wrapper