from flask_restful import Api
from app.resources.user import UserResource, UserListResources

api = Api()

api.add_resource(UserListResources, '/users')
api.add_resource(UserResource, '/users','/users/<user_id>')