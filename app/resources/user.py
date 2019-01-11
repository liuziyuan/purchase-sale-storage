from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from app.models.user import User


def abort_if_user_doesnt_exist(user, user_id):
    if user is None:
        abort(404, message="User {} doesn't exist".format(user_id))

fields = {
    'name': fields.String,
    'password': fields.String,
    'sign_in_count': fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Name cannot be blank!")
parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")

class UserResource(Resource):

    @marshal_with(fields)
    def get(self, user_id):
        user = User().get_by_id(user_id)
        abort_if_user_doesnt_exist(user, user_id)
        return user

    def delete(self, user_id):
        user = User().get_by_id(user_id)
        abort_if_user_doesnt_exist(user, user_id)
        user.delete()
        return '', 204

    @marshal_with(fields)
    def put(self, user_id):
        args = parser.parse_args()
        user = User().get_by_id(user_id)
        user.name = args['name']
        user.password = args['password']
        user.update()
        # TODOS[todo_id] = task
        return user, 201
    
    @marshal_with(fields)
    def post(self):
        args = parser.parse_args()
        user = User(name=args['name'], 
        password=args['password'], 
        sign_in_count=0)
        # user.save()
        user.save()
        # User.create(user)
        return user, 201
    
class UserListResources(Resource):

    @marshal_with(fields)
    def get(self):
        return User().all()
    

