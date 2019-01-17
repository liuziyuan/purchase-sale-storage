from .flask import app
from flask_cors import CORS

cors = CORS()
cors_resources = r'/api/*'

cors.init_app(app, resources=cors_resources)