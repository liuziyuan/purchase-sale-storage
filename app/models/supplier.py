from . import db
from .base import BaseUser

class Supplier(BaseUser, db.Model):
    __tablename__ = 'supplieres'
    ship_address = db.Column(db.String(255))