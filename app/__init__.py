from flask import Flask
from app.routes import api
app = Flask(__name__)
api.init_app(app)

