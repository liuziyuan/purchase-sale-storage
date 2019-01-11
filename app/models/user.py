from . import db
from .base import Base

user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

class User(Base):
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    sign_in_count = db.Column(db.Integer, default=0)

    roles = db.relationship('Role', secondary=user_roles, lazy='subquery',
        backref=db.backref('users', lazy=True))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()


