from flask import Flask
from flask_script import Manager, prompt_bool, Command
from flask_migrate import Migrate, MigrateCommand
from app import App
from config.initializers.database import db, command
from app.models import *
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1qaz2wsx#EDC@127.0.0.1:5432/postgres'

my_app = App()
my_app.init_app(app)

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('dbset', command)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
