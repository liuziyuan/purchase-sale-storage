from . import db
from .base import TimestampMixin

user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
)

class User(TimestampMixin, db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    sign_in_count = db.Column(db.Integer, default=0)
    name = db.Column(db.String(30))

    roles = db.relationship('Role', secondary=user_roles, lazy='subquery',
        backref=db.backref('users', lazy=True))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def all(self):
        return self.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def get_by_id(self, id):
        return self.query.filter_by(id=id).first()
    
    def login(self, username, password):
        return self.query.filter_by(username=username, password=password).first()

    def get_by_username(self, username):
        return self.query.filter_by(username=username).first()

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()





