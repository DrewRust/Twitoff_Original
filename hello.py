#### --->below will run: prints hello world
#### FLASK_APP=hello.py flask run
#### add an "about" to http://127.0.0.1:5000/ shows "about me"
#### "ctrl" c  --->quits

#### from the Flask website hello world example
from flask import Flask

#### importing Flask object from Flask class passing in name of file hello.py
app = Flask(__name__)

#### running below if successful will show 200.  404 would be an error
#### "routes"
#### decorator '/' root directory
@app.route('/')
def hello_world():
    return 'Hello, World!'
#### about page inside root directory
@app.route('/about')
def about():
    return 'About me...'