from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'this is testing'

@app.route('/about')
def about():
    return 'About'
