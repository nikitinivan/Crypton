from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

# Init Mongo
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return jsonify({"message": request.get_json()})
    else:
        return render_template('login.html')

@app.route('/register')
def register():
    return 'register'

if __name__ == '__main__':
    app.run()
