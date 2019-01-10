from flask_restful import Api
from app.resources.test_resource import TestResource

routes = Api()
routes.add_resource(TestResource, '/')