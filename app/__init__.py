from flask import Flask
from app.routes import routes
app = Flask(__name__)
routes.init_app(app)

