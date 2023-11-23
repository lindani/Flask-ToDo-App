# backend/app/models.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db)

class Task(db.Model):
	__tablename__ = 'tasks'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(250), nullable=False)
	completed = db.Column(db.Boolean, default=False)

	def json(self):
		return {'id': self.id, 'title': self.title, 'description': self.description, 'completed': self.completed}
