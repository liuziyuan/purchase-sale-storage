from app import db
from .base import Base

class User(Base):
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    sign_in_count = db.Column(db.Integer, default=0)


