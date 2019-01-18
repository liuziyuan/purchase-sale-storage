from . import db
from datetime import datetime

# class Base(db.Model):
#     __abstract__ = True
    
#     id = db.Column(db.Integer, primary_key=True)
#     created_on = db.Column(db.DateTime, default=db.func.now())
#     updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class IdMixin(object):
    id = db.Column(db.Integer, primary_key=True)

class TimestampMixin(IdMixin):
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class BaseUser(IdMixin):
    name = db.Column(db.String(30))
    mobile_tel = db.Column(db.Integer)
    tel = db.Column(db.Integer)
    address = db.Column(db.String(255))