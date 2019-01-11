from . import db
from .base import TimestampMixin

class Role(TimestampMixin, db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)