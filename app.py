from flask import Flask, render_template, jsonify, request, url_for, redirect
import json
import requests
import os
from werkzeug.utils import secure_filename
# from flaskblog.models import Post, User
# from flask_login import  login_user, current_user, logout_user, login_requirements
# from flaskblog.form import loginF

app = Flask(__name__)


def load_institutions_data():
    with open('package.json') as json_file:
        return json.load(json_file)

@app.route("/")
def show():
    return render_template("login.html")

@app.route("/login")
def display():
    institutions_data = load_institutions_data()
    return render_template('index.html', institutions=institutions_data["institutions"])

@app.route("/signup")
def signUp():
    return render_template('signup.html')

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File successfully uploaded'