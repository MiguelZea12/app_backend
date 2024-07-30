from app.extensions import db
from datetime import datetime

class TokenBlockList(db.Model):
    __tablename__ = 'token_block_list'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, jti):
        self.jti = jti
