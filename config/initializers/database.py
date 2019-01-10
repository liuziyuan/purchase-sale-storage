from flask_script import Manager, Command, prompt_bool
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
command = Manager()


class drop(Command):  
    'drop database'  
    def run(self):  
        if prompt_bool("Are you sure you want to lose all your data"):
            db.drop_all()

class reset(Command):
    def run(self):  
        if prompt_bool("Are you sure you want to lose all your data"):
            db.drop_all()
            db.create_all()

class test(Command):  
    'test'  
    def run(self):  
        print('hello, this is test of dbset command moudle')


command.add_command('test', test)
command.add_command('reset', reset)
command.add_command('drop', drop)
