from flask import Flask, abort, render_template, jsonify, request, url_for, redirect
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

def load_institutions_data():
    try:
        with open('package.json') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {"institutions": []}
    except json.JSONDecodeError:
        return {"institutions": []}

@app.route("/")
def show():
    return render_template("login.html")

@app.route("/login")
def display():
    institutions_data = load_institutions_data()
    page = request.args.get('page', 1, type=int)
    per_page = 20
    total = len(institutions_data["institutions"])
    start = (page - 1) * per_page
    end = start + per_page
    paginated_institutions = institutions_data["institutions"][start:end]
    
    return render_template('index.html', 
                           institutions=paginated_institutions,
                           page=page, 
                           per_page=per_page, 
                           total=total)

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
    
@app.route('/campus/<code>')
def show_campus(code):
    institutions_data = load_institutions_data()
    for institution in institutions_data["institutions"]:
        if institution["code"] == code:
            template_path = institution["link"]
            try:
                return render_template(template_path, institution=institution)
            except Exception:
                abort(404)
    abort(404)

@app.route('/course/<course_code>')
def show_course(course_code):
    institutions_data = load_institutions_data()
    for institution in institutions_data["institutions"]:
        for course in institution.get("courses", []):
            if course["code"] == course_code:
                template_path = course["link"]
                try:
                    return render_template(template_path, course=course)
                except Exception:
                    abort(404)
    abort(404)