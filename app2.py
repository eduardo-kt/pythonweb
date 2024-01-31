from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Dynamic route
@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

# No terminal: flask --app app1 run
# ou no command prompt: set FLASK_APP=app1 >> flask run
# ou no powershell: $env: FLASK_APP = "app1"