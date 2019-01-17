from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from app.models.user import User
from app.utils.result_code import ResultCode

def abort_if_user_doesnt_exist(user, user_id):
    if user is None:
        abort(404, message="User {} doesn't exist".format(user_id))

resource_fields = {}
login_fields = {}

# base fields
token_fields = { 'token': fields.String }
code_fields = { 'code': fields.Integer }

# Nested Field
# user fields
user_fields = {}
user_fields['username'] = fields.String(attribute='username')
user_fields['password'] = fields.String(attribute='password')
user_fields['sign_in_count'] = fields.Integer(attribute='sign_in_count')

resource_fields['user'] = fields.Nested(user_fields)
resource_fields.update(code_fields)

login_fields.update(resource_fields)
login_fields.update(token_fields)

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help="User Name cannot be blank!")
parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")

class UserResource(Resource):

    @marshal_with(user_fields)
    def get(self, user_id):
        user = User().get_by_id(user_id)
        abort_if_user_doesnt_exist(user, user_id)
        return user

    def delete(self, user_id):
        user = User().get_by_id(user_id)
        abort_if_user_doesnt_exist(user, user_id)
        user.delete()
        return '', 204

    @marshal_with(user_fields)
    def put(self, user_id):
        args = parser.parse_args()
        user = User().get_by_id(user_id)
        user.username = args['username']
        user.password = args['password']
        user.update()
        # TODOS[todo_id] = task
        return user, 201
    
    @marshal_with(user_fields)
    def post(self):
        args = parser.parse_args()
        user = User(username=args['username'], 
        password=args['password'], 
        sign_in_count=0)
        # user.save()
        user.save()
        # User.create(user)
        return user, 201
    
class UserListResources(Resource):

    @marshal_with(user_fields)
    def get(self):
        return User().all()

class SessionResources(Resource):
    
    @marshal_with(login_fields)
    def post(self):
        args = parser.parse_args()
        user = User().login(args['username'], args['password'])
        code = ResultCode.SUCCESS
        result = { 'user': user, 'code': code, 'token': 'admin' }
        return result, 201
    
    

