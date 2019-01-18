from . import db
from .base import BaseUser


class Consumer(BaseUser, db.Model):
    __tablename__ = 'consumeres'
    delivery_address = db.Column(db.String(255))