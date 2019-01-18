from config.initializers.flask import app
from config.config import *
from config.initializers.cors import cors, cors_resources
from config.initializers.db import db
from config.initializers.jwt import jwt
from config.initializers.api import api
from config.initializers.db_migrate import migrate
from config.initializers.manager import manager

from app.router import api
import psycopg2

if __name__ == '__main__':
    manager.run()
