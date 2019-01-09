from flask_restful import Api
from app import app
from app.resources.hello_world import HelloWorld

api = Api(app)

api.add_resource(HelloWorld, '/')