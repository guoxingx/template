
from flask import jsonify

from . import main
from .. import tasks_loader


@main.route('/')
def index():
    task = tasks_loader.grab_carbens.delay()
    return jsonify({
        'id': task.id,
    })


@main.route('/status/<task_id>')
def status(task_id):
    task = tasks_loader.grab_carbens.AsyncResult(task_id)
    return jsonify({
        'id': task.id,
        'state': str(task.info),
    })
