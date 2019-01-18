from .flask import app
from flask_restful import Api
from functools import wraps
api = Api()

def inject(func):
    func()
    api.init_app(app)

# def resources(func):
#     @wraps(func)
#     def wrapper(*args, **kw):
#         func(*args, **kw)
#         api.init_app(app)
#     return wrapper

# class ApiExtended(Api):
#     def inject(self, func):
#         func()
#         self.init_app(app)


# api = ApiExtended()

# def resources(func):
#     @functools.wraps(func)
#     def wrapper(api):
#         print('call %s():' % func.__name__)
#         func(api)
#         api.init_app(app)
#     return wrapper