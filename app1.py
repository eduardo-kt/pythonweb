from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World! </h1>'

# Não é necessário 
# if __name__ == "__main__":
#    app.run()

# No terminal: flask --app app1 run
# ou no command prompt: set FLASK_APP=app1 >> flask run
# ou no powershell: $env: FLASK_APP = "app1"