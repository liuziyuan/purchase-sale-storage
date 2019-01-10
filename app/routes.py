from flask_restful import Api
from app.resources.test_resource import TestResource

api = Api()
api.add_resource(TestResource, '/')