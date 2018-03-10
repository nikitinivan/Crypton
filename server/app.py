from flask import Flask, render_template
from flask_pymongo import PyMongo

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

# Init Mongo
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/login')
def login():
    return 'login'

@app.route('/register')
def register():
    return 'register'

if __name__ == '__main__':
    app.run()
