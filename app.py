from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
# create secret key between user and the server
app.secret_key = 'lkwjdfwfdhwfdihwfh'

# create a route for home directory


@app.route('/')
def home():
    return render_template('home.html')

# create a route for your-url directory


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}

        # check file is not already exsited
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        if request.form['code'] in urls.keys():
            flash('That short name has already been taken')
            return redirect(url_for('home'))

        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save(
                '/computing/year 4/Flask_EssT/url-shortener/url-shortener' + full_name)
            urls[request.form['code']] = {'file': full_name}
        # save url shorten into json file
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))
