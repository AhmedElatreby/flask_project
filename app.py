from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# create a route for home directory


@app.route('/')
def home():
    return render_template('home.html')

# create a route for your-url directory


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))
