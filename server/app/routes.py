# backend/app/routes.py
from flask import Blueprint, request, jsonify, make_response
from .models import Task, db
import logging

logger = logging.getLogger(__name__)

tasks = Blueprint("tasks", __name__)

@tasks.route('/new', methods=['POST'])
def create_task():
	try:
		data = request.get_json()
		new_task = Task(title=data['title'], description=data['description'], completed=data['completed'])
		db.session.add(new_task)
		db.session.commit()
		return make_response(jsonify({'message': 'task created'}), 201)
	except Exception as e:
		return make_response(jsonify({'message': f'error creating task: {e}'}), 500)

@tasks.route('/', methods=['GET'])
def get_tasks():
	try:
		taska = Task.query.all()
		task_json_list = [task.json() for task in taska]
		return make_response(jsonify(task_json_list), 200)
	except Exception as e:
		logger.error(f"Error getting taska: {e}")
		return make_response(jsonify({'message': 'error getting taska'}), 500)
	
@tasks.route('/<int:id>', methods=['GET'])
def get_task(id):
	try:
		task = Task.query.filter_by(id=id).first()
		if task:
			return make_response(jsonify({'task': task.json()}), 200)
		return make_response(jsonify({'message': 'task not found'}), 404)
	except Exception as e:
		logger.error(f"Error getting a task: {e}")
		return make_response(jsonify({'message': 'error getting tasks'}), 500)

@tasks.route('/<int:id>', methods=['PUT'])
def update_task(id):
	try:
		task = Task.query.filter_by(id=id).first()
		if task:
			data = request.get_json()
			task.title = data['title']
			task.description = data['description']
			task.completed = data['completed']
			db.session.commit()
			return make_response(jsonify({'message': 'task updated'}), 200)
		return make_response(jsonify({'message': 'task not found'}), 404)
	except Exception as e:
		logger.error(f"Error updating a task: {e}")
		return make_response(jsonify({'message': 'error updating task'}), 500)

@tasks.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
	try:
		task = Task.query.filter_by(id=id).first()
		if task:
			db.session.delete(task)
			db.session.commit()
			return make_response(jsonify({'message': 'task deleted'}), 200)
		return make_response(jsonify({'message': 'task not found'}), 404)
	except Exception as e:
		logger.error(f"Error deleting a task: {e}")
		return make_response(jsonify({'message': 'error deleting tasks'}), 500)
