from app import app, db
from datetime import datetime


class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))
    image = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    finishdate = db.Column(db.DateTime, index = True)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    subtasks = db.relationship('subTask', backref='task',cascade = 'all, delete-orphan', lazy = 'dynamic')

class subTask(db.Model):
    __tablename__ = 'subTask'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    task_id = db.Column(db.Integer, db.ForeignKey('Task.id'))