from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_login import LoginManager
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
#Move to separate config file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'eygfyiTYTdseGD5EE578OD098A7534RFDD' #For development purposes only

db = SQLAlchemy(app)

import routes
from models import User

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    #return None 

bootstrap = Bootstrap(app)
moment = Moment(app)



if __name__ == '__main__':
    app.run(debug=True) #Dev environment
