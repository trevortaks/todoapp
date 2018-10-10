import os
import uuid
from datetime import datetime
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
#from werkzeug.utils import secure_filename
from models import Task, subTask, User
from forms import newTask, Activity, Login, SignUp
from app import app, db



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required 
def index():
    tasks=Task.query.filter_by(user_id=1).order_by(Task.timestamp.desc())
    return render_template('index.html', tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first_or_404()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUp()
    if form.validate_on_submit():
        file = form.profilepic.data
        filename = uuid.uuid4().hex
        file.save(os.path.join(os.path.abspath("static/"),'photos', filename))
        user = User(username = form.username.data,
                    email = form.email.data,
                    fullname = form.fullname.data,
                    profilepic = filename
                    )
        user.set_password(form.password1.data)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/add', methods=['GET','POST'])
def additem():
    form = newTask()
    if form.validate_on_submit():
        file = form.image.data
        filename = uuid.uuid4().hex
        file.save(os.path.join(os.path.abspath("static/"), 'photos', filename))
        task = Task(name=form.name.data, 
                    finishdate = form.finishdate.data,
                    image = filename,
                    user = current_user
                    )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('submit.html', form=form)
        


@app.route('/delete/<id>')
def deleteitem(task_id):
    task = Task.query.filter_by(task_id=id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/modify')
def modifyitem(id):
    # if form.validate_on_submit():
    #     task = Task.query.filter_by(id = id)
    pass

@app.route('/task/<id>', methods=['GET', 'POST'])
def viewtask(id):
    form = Activity()
    if form.validate_on_submit():
        subTasks = subTask(name = form.activity.data, task_id = id)
        db.session.add(subTasks)
        db.session.commit()
        return redirect(url_for('viewtask', id=id))
    task = Task.query.filter_by(id=id).first_or_404()
    subtask = task.subtasks
    return render_template('viewtask.html', task=task, subtask=subtask, form=form)

@app.route('/completed/<id>')
def completeTask(id):
    task = Task.query.filter_by(id=id).first_or_404()
    task.completed = True
    time = datetime.utcnow()
    print(time)
    task.finishdate = time
    db.session.commit()
    return redirect(url_for('viewtask', id=id))

