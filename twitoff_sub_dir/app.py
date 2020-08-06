#### ---> runs the app in the terminal:
#### FLASK_APP=twitoff_sub_dir:APP flask run
#### running flask shell will give you an interactive python environment
#### ---> how to interact with your database
####  FLASK_APP=twitoff_sub_dir:APP flask shell
#### creates an interactive shell
#### ---> then type: dir()
#### ---> then type: from twitoff_sub_dir.db_model import db, User, Tweet
#### now you have access to User and Tweet
#### ---> then type: db.init_app(app)
#### (above will associate db model with flask app)
#### ---> exit() gets you out of the shell env

from flask import Flask, render_template
#### import User class
from .db_model import db, User

#### where the initial app code will live


#### define function called create app
def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/andrewrust/Twitoff/twitoff_sub_dir/twitoff.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route('/')
    def root():
        #### render a template
        # return render_template('base.html', title='Home', users=User.query.all())
        return "Welcome to Twitoff!"

    return app