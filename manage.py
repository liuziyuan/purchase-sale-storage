# from flask import Flask
from flask_script import Manager, prompt_bool, Command
from flask_migrate import MigrateCommand

from config.initializers.flask import app
from config.initializers.cors import cors, cors_resources
from config.initializers.db import db
from config.initializers.db_migrate import migrate
from config.initializers.jwt import jwt
from config.initializers.api import api
from config.initializers.manager import manager

from app.router import api
import psycopg2

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1qaz2wsx#EDC@127.0.0.1:5432/postgres'
app.config['JWT_SECRET_KEY'] = 'super-secret'

# jwt.init_app(app)
# api.init_app(app)
# cors.init_app(app, resources=cors_resources)
# db.init_app(app)
# migrate.init_app(app, db)


# manager.add_command('dbset', command)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
