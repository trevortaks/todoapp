from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, ValidationError
from models import Task, subTask

class newTask(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired()], render_kw={"placeholder":"Task Name"})
    image = FileField('Task Image',render_kw={"placeholder":"Task Image"})
    finishdate = DateField('DatePicker')
    submit = SubmitField('Submit')

class Activity(FlaskForm):
    activity = StringField('Activity', render_kw={"placeholder":"Activity"})
    submit = SubmitField('Submit')
