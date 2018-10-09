from flask import render_template, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
from models import Task, subTask
from forms import newTask, Activity
from app import app, db
import os
import uuid


@app.route('/', methods=['GET', 'POST'])
def index():
    tasks=Task.query.order_by(Task.timestamp.desc())
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET','POST'])
def additem():
    form = newTask()
    if form.validate_on_submit():
        file = form.image.data
        filename = uuid.uuid4().hex
        file.save(os.path.join(os.path.abspath("static/"), 'photos', filename))
        task = Task(name=form.name.data, 
                    finishdate = form.finishdate.data,
                    image = filename
                    )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('submit.html', form=form)
        


@app.route('/delete/<id>')
def deleteitem(id):
    task = Task.query.filter_by(id = id).first_or_404()
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
    db.session.commit()
    return redirect(url_for('viewtask', id=id))

