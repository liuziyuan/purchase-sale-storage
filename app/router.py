from flask_restful import Api
from app.resources.user import UserResource, UserListResources, SessionResources
BASE_URI = '/api'

def get_url(part_url='', version=''):
    if version is '':
        return BASE_URI + part_url
    else:
        return BASE_URI + '/' + version + part_url

api = Api()

api.add_resource(UserListResources, get_url(part_url='/users'))
api.add_resource(UserResource, get_url(part_url='/users'), get_url(part_url='/users/<user_id>'))
api.add_resource(SessionResources, get_url(part_url='/sessions'), get_url(part_url='/sessions/<user_id>'))

# api.add_resource(UserListResources, '/users')
# api.add_resource(UserResource, '/users','/users/<user_id>')