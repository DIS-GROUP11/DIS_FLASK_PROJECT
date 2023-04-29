import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates',
            static_folder='static', static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/discover')
def discover():
    return render_template('discover.html')


@app.route('/about')
def about():
    return render_template('about-us.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    try:
        email = request.form['email']
        password = request.form['password']

        if email == '' or password == '':
            return render_template('login.html', error='Missing form data')

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE email=?', (email,))
        user = cur.fetchone()

        if user is None:
            return render_template('login.html', error='User does not exist')

        if user[1] != password:
            return render_template('login.html', error='Incorrect password')

        return render_template('welcome.html', user=email)
    except:
        return render_template('login.html', error='Missing form data')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    try:
        email = request.form['email']
        password = request.form['password']

        if email == '' or password == '':
            return render_template('register.html', error='Missing form data')

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE email=?', (email,))
        user = cur.fetchone()

        if user is not None:
            return render_template('register.html', error='User already exists')

        cur.execute(
            'INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
        conn.commit()

        return render_template('register_success.html', user=email)
    except:
        return render_template('register.html', error='Missing form data')
