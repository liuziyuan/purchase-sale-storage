from .flask import app
from flask_jwt_extended import JWTManager

jwt = JWTManager()
jwt.init_app(app)