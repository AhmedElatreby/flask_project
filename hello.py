from flask import Flask, render_template

app = Flask(__name__)

# create a route for home directory


@app.route('/')
def home():
    return render_template('home.html')

# create a route for about directory


@app.route('/about')
def about():
    return "this is About page!"
