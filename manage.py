from flask import Flask
from flask_script import Manager
from app import App
app = Flask(__name__)

my_app = App()
my_app.init_app(app)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()