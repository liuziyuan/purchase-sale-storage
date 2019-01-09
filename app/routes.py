from flask_restful import Api
from app.resources.hello_world import HelloWorld

api = Api()
api.add_resource(HelloWorld, '/')