from flask import Flask, render_template, request, jsonify, make_response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

from config import Configuration

import jwt
import uuid
import datetime

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
        auth = request.get_json()
        if not auth or not auth['username'] or not auth['password']:
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
        users = mongo.db.users
        user = users.find_one({'name': auth['username']})
        if not user:
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

        if check_password_hash(user['password'], auth['password']):
            token = jwt.encode({
                'public_id': user['public_id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
            }, app.config['SECRET_KEY'])
            return jsonify({'token': token.decode('utf-8')})
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        auth = request.get_json()
        if auth and auth['username'] and auth['password']:
            users = mongo.db.users
            existing_user = users.find_one({
                'username': auth['username']
            })
            if existing_user is None:
                hashed_password = generate_password_hash(
                        auth['password'],
                        method='sha256'
                    )
                users.insert({
                    'name': auth['username'],
                    'public_id': str(uuid.uuid4()),
                    'password': hashed_password,
                })
                return jsonify({'message': 'You have been successfully registered!'})
            return jsonify({'message': 'User with this username already exist!'}), 401
        return jsonify({'message': 'Problems with registration'}), 401
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run()
