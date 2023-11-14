from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Setup MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
users = db['users']

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = users.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        return render_template('dashboard.html', name=username)
    return 'Invalid username/password'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        users.insert_one({'username': username, 'email': email, 'password': hashed_password})
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return '<h1>Welcome</h1>'
    
if __name__ == '__main__':
    app.run(debug=True)
