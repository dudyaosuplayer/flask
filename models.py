from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ExampleNames(db.Model):
    __tablename__ = 'example_names'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    added_on = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'added_on': self.added_on
        }