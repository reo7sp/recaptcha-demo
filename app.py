from flask import Flask, request, render_template, redirect, url_for
from urllib.parse import quote
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    if request.method == 'GET':
        return redirect(url_for('index'))
    return render_template('demo.html', site_key=request.form['site-key'])


@app.route('/handler', methods=['POST'])
def handler():
    if request.method == 'GET':
        return redirect(url_for('index'))
    recaptcha_response = request.form['g-recaptcha-response']
    return render_template('handler.html', recaptcha_response=quote(recaptcha_response))
