from config.initializers.manager import manager
from config.config import *
from config.initializers.cors import cors, cors_resources
from config.initializers.db import db
from config.initializers.jwt import jwt
from config.initializers.api import api
from config.initializers.db_migrate import migrate

import psycopg2
import app


if __name__ == '__main__':
    manager.run()
