from . import db
from .base import TimestampMixin

user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

class User(TimestampMixin, db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    sign_in_count = db.Column(db.Integer, default=0)

    roles = db.relationship('Role', secondary=user_roles, lazy='subquery',
        backref=db.backref('users', lazy=True))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()



