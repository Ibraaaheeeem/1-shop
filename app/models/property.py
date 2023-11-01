from app import db
from sqlalchemy.dialects.postgresql import ARRAY

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    values = db.Column(db.String(1024), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'values': self.values.split(',')
        }