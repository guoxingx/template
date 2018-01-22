
from .db import db


class BaseModel(db.Model):
    """
    Base model include id, created_at, updated_at columns
    """
    __abstract__ = True

    created_at = db.Column(db.TIMESTAMP(timezone=True), nullable=False,
                        server_default=db.text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.TIMESTAMP(timezone=True), nullable=False,
                        server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    id = db.Column(db.Integer, primary_key=True)


class Spider(BaseModel):
    url = db.Column(db.String(255), index=True, unique=True)
    content = db.Column(db.Text())
    location = db.Column(db.String(63))
    name = db.Column(db.String(63))
    homepage = db.Column(db.String(255))
