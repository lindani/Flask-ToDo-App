from flask import Flask
from .config import Config
from .models import db
from .routes import tasks

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)  # Initializing db instance here
	app.app_context().push()

	app.register_blueprint(tasks, url_prefix="/api/tasks")

	return app

