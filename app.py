from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


def load_data():
    with open('package.json') as f:
        return json.load(f)

# print(load_data())

@app.route("/")
def show():
    return render_template("login.html")

@app.route("/login")
def display():
    # data = load_data()
    with open("package.json") as infor:
        data = jsonify(infor)
        print(data)
    return render_template("campus.html", data=data)
    
