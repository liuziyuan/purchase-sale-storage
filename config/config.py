
from config.initializers.flask import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1qaz2wsx#EDC@127.0.0.1:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['JWT_SECRET_KEY'] = 'super-secret'
