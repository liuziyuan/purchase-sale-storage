from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from app.models.user import User

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

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
        return user

    def delete(self, user_id):
        user = User().get_by_id(user_id)
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
    

