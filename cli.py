import os
from app import app,db
from models import Task, subTask

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Task' : Task, 'subTask' : subTask }