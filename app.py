from flask import Flask, abort, render_template, request
import json
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

# Load institutions data from JSON file
def load_institutions_data():
    try:
        with open('package.json') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
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
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Checking if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File successfully uploaded', 200
    return 'Invalid file type', 400

@app.route('/campus/<code>')
def show_campus(code):
    institutions_data = load_institutions_data()
    institution = next((inst for inst in institutions_data["institutions"] if inst["code"] == code), None)
    if institution:
        template_filename = f'{code}.html'
        template_folder = 'campus'
        
        # Log the template path for debugging
        print(f'Trying to render template: {template_folder}/{template_filename}')
        
        if os.path.exists(os.path.join(app.template_folder, template_folder, template_filename)):
            return render_template(os.path.join(template_folder, template_filename))
    abort(404)