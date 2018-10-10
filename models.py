from app import db, app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, index=True)
    fullname = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    profilepic = db.Column(db.String(256))
    task = db.relationship('Task', backref='user', lazy='dynamic', cascade = 'all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))
    image = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    finishdate = db.Column(db.DateTime, index = True)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    subtasks = db.relationship('subTask', backref='task',cascade = 'all, delete-orphan', lazy = 'dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

class subTask(db.Model):
    __tablename__ = 'subTask'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    task_id = db.Column(db.Integer, db.ForeignKey('Task.id'))

