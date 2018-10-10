from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from models import Task, subTask

class newTask(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired()], render_kw={"placeholder":"Task Name"})
    image = FileField('Task Image',render_kw={"placeholder":"Task Image"})
    finishdate = DateField('DatePicker', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Activity(FlaskForm):
    activity = StringField('Activity', validators=[DataRequired()], render_kw={"placeholder":" Add Task Activity"})
    submit = SubmitField('Add Activity')

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder":"Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder":"Password"})
    submit = SubmitField('Login') 

class SignUp(FlaskForm):
    profilepic = FileField('Profile Picture', render_kw={"placeholder":"Profile Pic"})
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder":"Username"})
    fullname = StringField('Full Name', validators=[DataRequired()], render_kw={"placeholder":"Full Name"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder":"Email"})
    password1 = PasswordField('Password1', validators=[DataRequired()], render_kw={"placeholder":"Password"})
    password2 = PasswordField('Password2', validators=[DataRequired(), EqualTo('password1')], render_kw={"placeholder": "Repeat Password"})
    submit = SubmitField('Sign Up')