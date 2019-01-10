from app import db
from .base import Base

class Role(Base):
    name = db.Column(db.String(80), unique=True, nullable=False)