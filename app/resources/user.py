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

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
    
    @marshal_with(fields)
    def post(self):
        args = parser.parse_args()
        user = User(name=args['name'], password=args['password'], sign_in_count=0)
        User.create(user)
        
        return user, 201
        # todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        # todo_id = 'todo%i' % todo_id
        # TODOS[todo_id] = {'task': args['task']}
        # return TODOS[todo_id], 201
    
class UserListResources(Resource):
    def get(self):
        return TODOS
    

