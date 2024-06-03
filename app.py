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

def sanitize_course_name(course_name):
    return course_name.replace('&', 'and').replace(' ', '_').lower()

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



#DEKUT
@app.route('/course/<course_name>')
def course_1(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'courses/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/dekut")
def dekut():
    return render_template("campus/DKUT.html")

#Eldoret
@app.route('/course_automating_folder_creating/ELDO POLY - ELDORET POLYTECHNIC/<course_name>')
def course_2(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/ELDO POLY - ELDORET POLYTECHNIC/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/eldoret")
def eldoret():
    return render_template("campus/DKUT.html")

#AIU
@app.route('/course_automating_folder_creating/AIUCourse/<course_name>')
def course_3(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/AIUCourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/AIU")
def AIU():
    return render_template("campus/AIU.html")

#ALDAI TTI
@app.route('/course_automating_folder_creating/ALDAITTICourse/<course_name>')
def course_4(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/ALDAITTICourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/ALDITTI")
def ALDITTI():
    return render_template("campus/ALDAITTI.html")

#ALUPE 
@app.route('/course_automating_folder_creating/ALUPECourse/<course_name>')
def course_5(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/ALUPECourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/ALUPE")
def AU():
    return render_template("campus/AU.html")

#ALUPE TVET
@app.route('/course_automating_folder_creating/AlupeTvetCourse/<course_name>')
def course_6(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/AlupeTvetCourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/AU-TVET")
def AU_TVET():
    return render_template("campus/AU TVET.html")

#AMIU
@app.route('/course_automating_folder_creating/AMIUCourse/<course_name>')
def course_7(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/AMIUCourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/AMIU")
def AMIU():
    return render_template("campus/AMIU.html")

#ASMTTI TTI
@app.route('/course_automating_folder_creating/ASM-TTICourse/<course_name>')
def course_8(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/ASM-TTICourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

def ASMTTI():
    return render_template("campus/ASM TTI.html")

#BAC BUKURA
@app.route('/course_automating_folder_creating/BAC - BUKURA AGRICULTURAL COLLEGE/<course_name>')
def course_9(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/BAC - BUKURA AGRICULTURAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/BAC")
def BAC():
    return render_template("campus/BAC TVC.html")

#BAHATI IBSA 
@app.route('/course_automating_folder_creating/Bahati-IbasCourse/<course_name>')
def course_10(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/Bahati-IbasCourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/BAHATI-IBSA")
def BAHATI_IBSA():
    return render_template("campus/BAHATI IBSA.html")


#BARA TTI
@app.route('/course_automating_folder_creating/BARA - UNIVERSITY OF EASTERN AFRICA, BARATON/<course_name>')
def course_11(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/BARA - UNIVERSITY OF EASTERN AFRICA, BARATON/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/BARA")
def BARA():
    return render_template("campus/BARA.html")

#CU
@app.route('/course_automating_folder_creating/CU - CHUKA UNIVERSITY/<course_name>')
def course_12(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/CU - CHUKA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/CU")
def CU():
    return render_template("campus/CU.html")

#CUK NAIROBI CBD TI
@app.route('/course_automating_folder_creating/CUK NAIROBI CBD TI - THE CUK NAIROBI CBD TRAINING INSTITUTE/<course_name>')
def course_13(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/CUK NAIROBI CBD TI - THE CUK NAIROBI CBD TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/CUK-NAIROBI-CBD-TI")
def CUKCBD():
    return render_template("campus/CUK-NAIROBI-CBD-TI.html")

#JKUAT
@app.route('/course_automating_folder_creating/JKUATCourse/<course_name>')
def course_14(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/JKUATCourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/JKUAT")
def JKUAT():
    return render_template("campus/JKUAT.html")

#KABIANGA
@app.route('/course_automating_folder_creating/KABIANGA - KABIANGA UNIVERSITY/<course_name>')
def course_15(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/KABIANGA - KABIANGA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/KABIANGA")
def KABIANGA():
    return render_template("campus/KABIANGA.html")

#KARATINA
@app.route('/course_automating_folder_creating/karatinaCourse/<course_name>')
def course_16(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/karatinaCourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/KARATINA")
def KARATINA():
    return render_template("campus/KARATINA.html")

#KIRINYAGA - KYU
@app.route('/course_automating_folder_creating/KYU - KIRINYAGA UNIVERSITY/<course_name>')
def course_17(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/KYU - KIRINYAGA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/KYU")
def KYU():
    return render_template("campus/KYU.html")

#LUKENYA - LU
@app.route('/course_automating_folder_creating/LUKENYA - LUKENYA UNIVERSITY/<course_name>')
def course_18(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/LUKENYA - LUKENYA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/LU")
def LU():
    return render_template("campus/LU.html")

#MCKU
@app.route('/course_automating_folder_creating/MCKUcourse/<course_name>')
def course_19(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MCKUcourse/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MCKU")
def MCKU():
    return render_template("campus/MCKU.html")

# MERTI TTI
@app.route('/course_automating_folder_creating/MERTI TTI - MERTI TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_20(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MERTI TTI - MERTI TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MERTI")
def MERTI():
    return render_template("campus/MERTI TTI.html")

# MERU POLY
@app.route('/course_automating_folder_creating/MERU POLY - MERU NATIONAL POLYTECHNIC/<course_name>')
def course_21(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MERU POLY - MERU NATIONAL POLYTECHNIC/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MERU-POLY")
def MERUPOLY():
    return render_template("campus/MERU POLY.html")

# MICHUKI TTI
@app.route('/course_automating_folder_creating/MICHUKI TTI - MICHUKI TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_22(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MICHUKI TTI - MICHUKI TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MICHUKI")
def MICHUKI():
    return render_template("campus/MICHUKI TTI.html")

# MITUNGUU TTI
@app.route('/course_automating_folder_creating/MITUNGUU TTI - MITUNGUU TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_23(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MITUNGUU TTI - MITUNGUU TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MITUNGUU")
def MITUNGUU():
    return render_template("campus/MITUNGUU TTI.html")

# MKU
@app.route('/course_automating_folder_creating/MKU - MOUNT KENYA UNIVERSITY/<course_name>')
def course_24(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MKU - MOUNT KENYA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MKU")
def MKU():
    return render_template("campus/MKU.html")

# MMU
@app.route('/course_automating_folder_creating/MMU - MULTIMEDIA UNIVERSITY OF KENYA/<course_name>')
def course_25(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MMU - MULTIMEDIA UNIVERSITY OF KENYA/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MMU")
def MMU():
    return render_template("campus/MMU.html")

# MMUST
@app.route('/course_automating_folder_creating/MMUST - MASINDE MULIRO UNIVERSITY OF SCIENCE & TECHNOLOGY/<course_name>')
def course_26(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MMUST - MASINDE MULIRO UNIVERSITY OF SCIENCE & TECHNOLOGY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MMUST")
def MMUST():
    return render_template("campus/MMUST.html")

# MOCHONGOI TVC
@app.route('/course_automating_folder_creating/MOCHONGOI TVC - MOCHONGOI TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_27(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MOCHONGOI TVC - MOCHONGOI TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MOCHONGOI-TVC")
def MOCHONGOI():
    return render_template("campus/MOCHONGOI TVC.html")

# MOIBEN TVC
@app.route('/course_automating_folder_creating/MOIBEN TVC - MOIBEN TECHNICAL VOCATIONAL COLLEGE/<course_name>')
def course_28(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MOIBEN TVC - MOIBEN TECHNICAL VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MOIBEN-TVC")
def MOIBEN():
    return render_template("campus/MOIBEN TVC.html")

# MOlO TVC
@app.route('/course_automating_folder_creating/MOLO TVC - MOLO TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_29(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MOLO TVC - MOLO TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MOlO-TVC")
def MOlO():
    return render_template("campus/MOlO TVC.html")

# MORENDAT
@app.route('/course_automating_folder_creating/MORENDAT - MORENDAT INSTITUTE OF OIL AND GAS/<course_name>')
def course_30(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MORENDAT - MORENDAT INSTITUTE OF OIL AND GAS/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MORENDAT")
def MORENDAT():
    return render_template("campus/MORENDAT.html")

# MSABWENI TVC
@app.route('/course_automating_folder_creating/MSAMBWENI TVC - MSAMBWENI TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_31(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MSAMBWENI TVC - MSAMBWENI TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MSAMBWENI")
def MSAMBWENI():
    return render_template("campus/MSAMBWENI TVC.html")

# MSU
@app.route('/course_automating_folder_creating/MSU - MASENO UNIVERSITY/<course_name>')
def course_32(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MSU - MASENO UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

# @app.route("/Maseno")
# def MERUPOLY():
#     return render_template("campus/MSU.html")

# MU
@app.route('/course_automating_folder_creating/MU - MOI UNIVERSITY/<course_name>')
def course_33(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MU - MOI UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MU")
def MU():
    return render_template("campus/MU.html")

# MUKIRA TTI
@app.route('/course_automating_folder_creating/MUKIRIA TTI - MUKIRIA TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_34(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MUKIRIA TTI - MUKIRIA TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MUKIRA-TTI")
def MUKIRA():
    return render_template("campus/MUKIRA TTI.html")

# MUKURWEINI
@app.route('/course_automating_folder_creating/MUKURWEINI TTI - MUKURWEINI TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_35(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MUKURWEINI TTI - MUKURWEINI TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MUKURWEINI-TTI")
def MUKURWEINI():
    return render_template("campus/MUKURWEINI TTI.html")

# MULANGO TVC
@app.route('/course_automating_folder_creating/MULANGO TVC - MULANGO TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_36(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MULANGO TVC - MULANGO TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MULANGO-TVC")
def MULANGO():
    return render_template("campus/MULANGO TVC.html")

# MUMIAS WEST TVC
@app.route('/course_automating_folder_creating/MUMIAS WEST TVC - MUMIAS WEST TECHNICAL VOCATIONAL COLLEGE/<course_name>')
def course_37(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MUMIAS WEST TVC - MUMIAS WEST TECHNICAL VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MUMIA-WEST-TVC")
def MUMIAWEST():
    return render_template("campus/MUMIAS WEST TVC.html")

# MUNGATSI TVC
@app.route('/course_automating_folder_creating/MUNGATSI TVC - MUNGATSI TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_38(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MUNGATSI TVC - MUNGATSI TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MUNGATSI-TVC")
def MUNGATSI():
    return render_template("campus/MUNGATSI TVC.html")

# MURAGA TVC
@app.route('/course_automating_folder_creating/MURAGA TVC - MURAGA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_39(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MURAGA TVC - MURAGA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MURAGA-TVC")
def MURAGA():
    return render_template("campus/MURAGA TVC.html")

# MURANG'A TTI
@app.route('/course_automating_folder_creating/MURANGA TTI - MURANGA TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_40(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MURANGA TTI - MURANGA TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MURANG'A-TTI")
def MURANGA():
    return render_template("campus/MURANGA TTI.html")

# MURANGA UNIVERSITY TI
@app.route('/course_automating_folder_creating/MURANGA UNIVERSITY TI - MURANGA UNIVERSITY OF TECHNOLOGY TVET INSTITUTE/<course_name>')
def course_41(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MURANGA UNIVERSITY TI - MURANGA UNIVERSITY OF TECHNOLOGY TVET INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MURANGA-VERSITY")
def MURANGAVERSITY():
    return render_template("campus/MURANGA UNIVERSITY TI.html")


# MUSAKASA TTI
@app.route('/course_automating_folder_creating/MUSAKASA TTI - MUSAKASA TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_42(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MUSAKASA TTI - MUSAKASA TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MUSAKASA-TTI")
def MUSAKASA():
    return render_template("campus/MUSAKASA TTI.html")


# MUST
@app.route('/course_automating_folder_creating/MUST - MERU UNIVERSITY OF SCIENCE AND TECHNOLOGY/<course_name>')
def course_43(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MUST - MERU UNIVERSITY OF SCIENCE AND TECHNOLOGY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MUST")
def MUST():
    return render_template("campus/MUST.html")

# MUT
@app.route('/course_automating_folder_creating/MUT - MURANGA UNIVERSITY OF TECHNOLOGY/<course_name>')
def course_44(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MUT - MURANGA UNIVERSITY OF TECHNOLOGY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

# @app.route("/MUT")
# def MUST():
#     return render_template("campus/MUT.html")

# MWALA TVC
@app.route('/course_automating_folder_creating/MWALA TVC - MWALA TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_45(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MWALA TVC - MWALA TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MWALA-TVC")
def MWALA():
    return render_template("campus/MWALA TVC.html")

# MWEA TVC
@app.route('/course_automating_folder_creating/MWEA TVC - MWEA TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_46(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/MWEA TVC - MWEA TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/MWEA-TVC")
def MWEA():
    return render_template("campus/MWEA TVC.html")

# NACHU TVC
@app.route('/course_automating_folder_creating/NACHU TVC - NACHU TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_47(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NACHU TVC - NACHU TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NACHU-TVC")
def NACHU():
    return render_template("campus/NACHU TVC.html")

# NAIROBI TTI
@app.route('/course_automating_folder_creating/NAIROBI TTI - NAIROBI TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_48(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NAIROBI TTI - NAIROBI TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NAIROBI-TTI")
def NAIROBITTI():
    return render_template("campus/NAIROBI TTI.html")

# NAIVASHA TVC
@app.route('/course_automating_folder_creating/NAIVASHA TVC - NAIVASHA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_49(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NAIVASHA TVC - NAIVASHA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NAIVASHA-TVC")
def NAIVASHATVC():
    return render_template("campus/NAIVASHA TVC.html")

# NAROK WEST TTI TTI
@app.route('/course_automating_folder_creating/NAROK WEST TTI - NAROK WEST TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_50(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NAROK WEST TTI - NAROK WEST TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NAROKWEST")
def NAROKWEST():
    return render_template("campus/NAROK WEST TTI.html")

# NAVAKHOLO TVC
@app.route('/course_automating_folder_creating/NAVAKHOLO TVC - NAVAKHOLO TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_51(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NAVAKHOLO TVC - NAVAKHOLO TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NAVAKHOLO")
def NAVAKHOLO():
    return render_template("campus/NAVAKHOLO TVC.html")

# NDARAGWA TVC
@app.route('/course_automating_folder_creating/NDARAGWA TVC - NDARAGWA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_52(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NDARAGWA TVC - NDARAGWA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NDARAGWA")
def NDARAGWA():
    return render_template("campus/NDARAGWA TVC.html")

# NDIA TVC
@app.route('/course_automating_folder_creating/NDIA TVC - NDIA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_53(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NDIA TVC - NDIA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NDIA")
def NDIA():
    return render_template("campus/NDIA TVC.html")

# NEPOLY
@app.route('/course_automating_folder_creating/NEPOLY - NORTH EASTERN NATIONAL POLYTECHNIC/<course_name>')
def course_54(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NEPOLY - NORTH EASTERN NATIONAL POLYTECHNIC/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

# @app.route("/NEPOLY")
# def MUST():
#     return render_template("campus/NEPOLY.html")

# NGONG TVC
@app.route('/course_automating_folder_creating/NGONG TVC - NGONG TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_55(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NGONG TVC - NGONG TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NGONG-TVC")
def NGONGTVC():
    return render_template("campus/NGONG TVC.html")


# NJORO TTI
@app.route('/course_automating_folder_creating/NJORO TTI - NJORO TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_njoro(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NJORO TTI - NJORO TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NJOROTTI")
def NJORO():
    return render_template("campus/NJORO TTI.html")

# NKABUNE TTI
@app.route('/course_automating_folder_creating/NKABUNE TTI - NKABUNE TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_57(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NKABUNE TTI - NKABUNE TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NKABUNE")
def NKABUNE():
    return render_template("campus/NKABUNE TTI.html")

# NORTH HORR TVC
@app.route('/course_automating_folder_creating/NORTH HORR TVC - NORTH HORR TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_58(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NORTH HORR TVC - NORTH HORR TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NORTH-HORR")
def NORTHHORR():
    return render_template("campus/NORTH HORR TVC.html")

# NUU TVC
@app.route('/course_automating_folder_creating/NUU TVC - NUU TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_59(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NUU TVC - NUU TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NUU")
def NUU():
    return render_template("campus/NUU TVC.html")

# NYAKACH TVC
@app.route('/course_automating_folder_creating/NYAKACH TVC - NYAKACH TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_60(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NYAKACH TVC - NYAKACH TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NYAKACH")
def NYAKACH():
    return render_template("campus/NYAKACH TVC.html")

# NYANDARUA POLY
@app.route('/course_automating_folder_creating/NYANDARUA POLY - NYANDARUA NATIONAL POLYTECHNIC/<course_name>')
def course_nyandarua(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NYANDARUA POLY - NYANDARUA NATIONAL POLYTECHNIC/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NYANDARUA")
def NYANDARUA():
    return render_template("campus/NYANDARUA POLY.html")

# NYERI POLY
@app.route('/course_automating_folder_creating/NYERI POLY - NYERI NATIONAL POLYTECHNIC/<course_name>')
def course_61(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/NYERI POLY - NYERI NATIONAL POLYTECHNIC/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/NYERI")
def NYERI():
    return render_template("campus/NYERI POLY.html")

# OKAME TVC
@app.route('/course_automating_folder_creating/OKAME TVC - OKAME TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_62(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/OKAME TVC - OKAME TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/OKAME")
def OKAME():
    return render_template("campus/OKAME TVC.html")

# OLLESSOS TTI
@app.route('/course_automating_folder_creating/OLLESSOS TTI - OLLESSOS TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_63(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/OLLESSOS TTI - OLLESSOS TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/OLLESSOS")
def OLLESSOS():
    return render_template("campus/OLLESSOS TTI.html")

# OMUGA TVC
@app.route('/course_automating_folder_creating/OMUGA TVC - OMUGA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_64(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/OMUGA TVC - OMUGA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/OMUGA")
def OMUGA():
    return render_template("campus/OMUGA TVC.html")

# OROGARE TVC
@app.route('/course_automating_folder_creating/OROGARE TVC - OROGARE TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_65(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/OROGARE TVC - OROGARE TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/OROGARE")
def OROGARE():
    return render_template("campus/OROGARE TVC.html")

# PAC
@app.route('/course_automating_folder_creating/PAC - PAN AFRICA CHRISTIAN UNIVERSITY/<course_name>')
def course_66(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/PAC - PAN AFRICA CHRISTIAN UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/PAC")
def PAC():
    return render_template("campus/PAC.html")

# PCKINYANJUI TTI
@app.route('/course_automating_folder_creating/PCKINYANJUI TTI - PC KINYANJUI TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_67(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/PCKINYANJUI TTI - PC KINYANJUI TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/PCKINYANJUI")
def PCKINYANJUI():
    return render_template("campus/PCKINYANJUI TTI.html")

# PIU
@app.route('/course_automating_folder_creating/PIU - PIONEER INTERNATIONAL UNIVERSITY/<course_name>')
def course_68(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/PIU - PIONEER INTERNATIONAL UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/PIU")
def PIU():
    return render_template("campus/PIU.html")

# PU
@app.route('/course_automating_folder_creating/PU - PWANI UNIVERSITY/<course_name>')
def course_69(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/PU - PWANI UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/PU")
def PU():
    return render_template("campus/PU.html")

# PUEA
@app.route('/course_automating_folder_creating/PUEA - PRESBYTERIAN UNIVERSITY OF EAST AFRICA/<course_name>')
def course_70(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/PUEA - PRESBYTERIAN UNIVERSITY OF EAST AFRICA/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/PUEA")
def PUEA():
    return render_template("campus/PUEA.html")

# RACHUNYO TVC
@app.route('/course_automating_folder_creating/RACHUONYO TVC - RACHUONYO TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_71(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RACHUONYO TVC - RACHUONYO TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RACHUONYO")
def RACHUONYO():
    return render_template("campus/RACHUONYO TVC.html")

# RANGWE TVC
@app.route('/course_automating_folder_creating/RANGWE TVC - RANGWE TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_72(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RANGWE TVC - RANGWE TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RANGWE")
def RANGWE():
    return render_template("campus/RANGWE TVC.html")

# RCMRD
@app.route('/course_automating_folder_creating/RCMRD - REGIONAL CENTRE FOR MAPPING OF RESOURCES FOR DEVELOPMENT/<course_name>')
def course_73(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RCMRD - REGIONAL CENTRE FOR MAPPING OF RESOURCES FOR DEVELOPMENT/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RCMRD")
def RCMRD():
    return render_template("campus/RCMRD.html")

# RIAMO TVC
@app.route('/course_automating_folder_creating/RIAMO TVC - RIAMO TECHNICAL VOCATIONAL COLLEGE/<course_name>')
def course_74(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RIAMO TVC - RIAMO TECHNICAL VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RIAMO")
def RIAMO():
    return render_template("campus/RIAMO TVC.html")

# RIAT
@app.route('/course_automating_folder_creating/RIAT - RAMOGI INSTITUTE OF ADVANCE TECHNOLOGY/<course_name>')
def course_75(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RIAT - RAMOGI INSTITUTE OF ADVANCE TECHNOLOGY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RIAT")
def RIAT():
    return render_template("campus/RIAT.html")

# RIATIRIMBA TVC
@app.route('/course_automating_folder_creating/RIATIRIMBA TVC - RIATIRIMBA TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_76(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RIATIRIMBA TVC - RIATIRIMBA TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RIATIRIMBA")
def RIATIRIMBA():
    return render_template("campus/RIATIRIMBA TVC.html")

# RIFT VALLEY TTI
@app.route('/course_automating_folder_creating/RIFT VALLEY TTI - RIFT VALLEY TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_77(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RIFT VALLEY TTI - RIFT VALLEY TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RIFTVALLEY")
def RIFTVALLEY():
    return render_template("campus/RIFT VALLEY TTI.html")

# RIRAGIA TTI
@app.route('/course_automating_folder_creating/RIRAGIA TTI - RIRAGIA TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_78(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RIRAGIA TTI - RIRAGIA TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RIRAGIA")
def RIRAGIA():
    return render_template("campus/RIRAGIA TTI.html")

# RONGO -RNU
@app.route('/course_automating_folder_creating/RNU - RONGO UNIVERSITY/<course_name>')
def course_79(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RNU - RONGO UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RONGO")
def RONGO():
    return render_template("campus/RONGO UNIVERSITY TI.html")

# RTI
@app.route('/course_automating_folder_creating/RTI - RAILWAY TRAINING INSTITUTE/<course_name>')
def course_80(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RTI - RAILWAY TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RTI")
def RTI():
    return render_template("campus/RTI.html")

# RU
@app.route('/course_automating_folder_creating/RU - RIARA UNIVERSITY/<course_name>')
def course_81(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RU - RIARA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RU")
def RU():
    return render_template("campus/RU.html")

# RUIRU TVC
@app.route('/course_automating_folder_creating/RUIRU TVC - RUIRU TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_82(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RUIRU TVC - RUIRU TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RUIRU-TVC")
def RUIRUTVC():
    return render_template("campus/RUIRU TVC.html")

# RUNYEJES TVC
@app.route('/course_automating_folder_creating/RUNYENJES TVC - RUNYENJES TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_83(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RUNYENJES TVC - RUNYENJES TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RUNYENJES")
def RUNYEJES():
    return render_template("campus/RUNYEJES TVC.html")

# RVIST
@app.route('/course_automating_folder_creating/RVIST - RIFT VALLEY INSTITUTE OF SCIENCE AND TECHNOLOGY/<course_name>')
def course_84(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/RVIST - RIFT VALLEY INSTITUTE OF SCIENCE AND TECHNOLOGY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/RVIST")
def RVIST():
    return render_template("campus/RVIST.html")

# SABATIA TVC
@app.route('/course_automating_folder_creating/SABATIA TVC - SABATIA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_85(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SABATIA TVC - SABATIA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SABATIA")
def SABATIA():
    return render_template("campus/SABATIA TVC.html")

# SABU
@app.route('/course_automating_folder_creating/SABU - SABU TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_86(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SABU - SABU TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SABU")
def SABU():
    return render_template("campus/SABU.html")

# SAGANA TVC
@app.route('/course_automating_folder_creating/SAGANA TVC - SAGANA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_87(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SAGANA TVC - SAGANA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SAGANA")
def SAGANA():
    return render_template("campus/SAGANA TVC.html")

# SAIKERI TVC
@app.route('/course_automating_folder_creating/SAIKERI TVC - SAIKERI TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_88(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SAIKERI TVC - SAIKERI TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SAIKERI")
def SAIKERI():
    return render_template("campus/SAIKERI TVC.html")

# SAIMO KIPSARAMAN TVC
@app.route('/course_automating_folder_creating/SAIMO KIPSARAMAN TVC - SAIMO KIPSARAMAN TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_89(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SAIMO KIPSARAMAN TVC - SAIMO KIPSARAMAN TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SAIMO-KIPSARAMAN")
def SAIMO_KIPSARAMAN():
    return render_template("campus/SAIMO KIPSARAMAN TVC.html")

# SAKWA TVC
@app.route('/course_automating_folder_creating/SAKWA TVC - SAKWA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_90(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SAKWA TVC - SAKWA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SAKWA")
def SAKWA():
    return render_template("campus/SAKWA TVC.html")

# SAMBURU TTI
@app.route('/course_automating_folder_creating/SAMBURU TTI - SAMBURU TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_91(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SAMBURU TTI - SAMBURU TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SAMBURU")
def SAMBURU():
    return render_template("campus/SAMBURU TTI.html")

# SANGALO
@app.route('/course_automating_folder_creating/SANGALO TTI - SANGALO TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_92(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SANGALO TTI - SANGALO TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SANGALO")
def SANGALO():
    return render_template("campus/SANGALO TTI.html")

# SAUNI TVC
@app.route('/course_automating_folder_creating/SAUNI TVC - SAUNI TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_93(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SAUNI TVC - SAUNI TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SAUNI")
def SAUNI():
    return render_template("campus/SAUNI TVC.html")

# SCIE
@app.route('/course_automating_folder_creating/SCIE - SIGALAGALA NATIONAL POLYTECHNIC/<course_name>')
def course_94(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SCIE - SIGALAGALA NATIONAL POLYTECHNIC/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SCIE")
def SCIE():
    return render_template("campus/SCIE.html")

# SEKU
@app.route('/course_automating_folder_creating/SEKU - SOUTH EASTERN KENYA UNIVERSITY/<course_name>')
def course_95(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SEKU - SOUTH EASTERN KENYA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SEKU")
def SEKU():
    return render_template("campus/SEKU.html")

# SHANZU TTI
@app.route('/course_automating_folder_creating/SHANZU TTI - SHANZU TEACHERS TRAINING COLLEGE/<course_name>')
def course_96(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SHANZU TTI - SHANZU TEACHERS TRAINING COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SHANZU")
def SHANZU():
    return render_template("campus/SHANZU TTI.html")

# SIGOR TTI
@app.route('/course_automating_folder_creating/SIGOR TTI - SIRISIA TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_97(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SIGOR TTI - SIRISIA TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SIGOR-TTI")
def SIGOR_TTI():
    return render_template("campus/SIGOR TTI.html")

# SIGOR TVC
@app.route('/course_automating_folder_creating/SIGOR TVC - SIGOR TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_98(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SIGOR TVC - SIGOR TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SIGOR-TVC")
def SIGOR_TVC():
    return render_template("campus/SIGOR TVC.html")

# SIT
@app.route('/course_automating_folder_creating/SIT - SIKRI TECHNICAL TRAINING INSTITUTE FOR THE BLIND AND DEAF/<course_name>')
def course_99(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SIT - SIKRI TECHNICAL TRAINING INSTITUTE FOR THE BLIND AND DEAF/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SIT")
def SIT():
    return render_template("campus/SIT.html")

# SITTV
@app.route('/course_automating_folder_creating/SITTV - SIKRI TECHNICAL AND VOCATIONAL COLLEGE FOR THE BLIND AND DEAF/<course_name>')
def course_100(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SITTV - SIKRI TECHNICAL AND VOCATIONAL COLLEGE FOR THE BLIND AND DEAF/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SITTV")
def SITTV():
    return render_template("campus/SITTV.html")

# SPU
@app.route('/course_automating_folder_creating/SPU - ST PAULS UNIVERSITY/<course_name>')
def course_101(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/SPU - ST PAULS UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/SPU")
def SPU():
    return render_template("campus/SPU.html")

# ST JOSEPH TI
@app.route('/course_automating_folder_creating/ST.JOSEPH TI - ST JOSEPHS TECHNICAL INSTITUTE FOR THE DEAF NYANGOMA/<course_name>')
def course_102(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/ST.JOSEPH TI - ST JOSEPHS TECHNICAL INSTITUTE FOR THE DEAF NYANGOMA/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/ST-JOSEPH")
def ST_JOSEPH():
    return render_template("campus/ST.JOSEPH TI.html")

# TANA RIVER TVC
@app.route('/course_automating_folder_creating/TANA RIVER TVC - TANA RIVER TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_103(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TANA RIVER TVC - TANA RIVER TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TANA_RIVER")
def TANA_RIVER():
    return render_template("campus/TANA RIVER TVC.html")

# TAVETA TVC
@app.route('/course_automating_folder_creating/TAVETA TVC - TAVETA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_104(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TAVETA TVC - TAVETA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TAVETA")
def TAVETA():
    return render_template("campus/TAVETA TVC.html")

# TEAU TVC
@app.route('/course_automating_folder_creating/TEAU - THE EAST AFRICAN UNIVERSITY/<course_name>')
def course_105(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TEAU - THE EAST AFRICAN UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TEAU")
def TEAU():
    return render_template("campus/TEAU.html")

# TETU TVC
@app.route('/course_automating_folder_creating/TETU TVC - TETU TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_106(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TETU TVC - TETU TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TETU")
def TETU():
    return render_template("campus/TETU TVC.html")

# THARAKA TVC
@app.route('/course_automating_folder_creating/THARAKA TVC - THARAKA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_107(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/THARAKA TVC - THARAKA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/THARAKA")
def THARAKA():
    return render_template("campus/THARAKA TVC.html")

# THARAKA UNIVERSITY
@app.route('/course_automating_folder_creating/THARAKA UNIVERSITY TI - THARAKA UNIVERSITY TVET INSTITUTE/<course_name>')
def course_108(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/THARAKA UNIVERSITY TI - THARAKA UNIVERSITY TVET INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/THARAKA-VERSITY")
def THARAKA_VERSITY():
    return render_template("campus/THARAKA UNIVERSITY TI.html")

# THIKA TTI
@app.route('/course_automating_folder_creating/THIKA TTI - THIKA TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_109(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/THIKA TTI - THIKA TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/THIKA-TTI")
def THIKA_TTI():
    return render_template("campus/THIKA TTI.html")

# THRKU
@app.route('/course_automating_folder_creating/THRKU - THARAKA UNIVERSITY/<course_name>')
def course_110(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/THRKU - THARAKA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/THRKU")
def THRKU():
    return render_template("campus/THRKU.html")

# TIGANIA EAST TVC
@app.route('/course_automating_folder_creating/TIGANIA EAST TVC - TIGANIA EAST TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_111(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TIGANIA EAST TVC - TIGANIA EAST TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TIGANIA-EAST")
def TIGANIA_EAST():
    return render_template("campus/TIGANIA EAST TVC.html")

# TINDIRET TVC
@app.route('/course_automating_folder_creating/TINDIRET TVC - TINDIRET TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_112(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TINDIRET TVC - TINDIRET TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TINDIRET")
def TINDIRET():
    return render_template("campus/TINDIRET TVC.html")

# TMU
@app.route('/course_automating_folder_creating/TMU - TOM MBOYA UNIVERSITY/<course_name>')
def course_113(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TMU - TOM MBOYA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TMU")
def TMU():
    return render_template("campus/TMU.html")

# TOMBOYA LC
@app.route('/course_automating_folder_creating/TOMBOYA LC - TOM MBOYA LABOUR COLLEGE/<course_name>')
def course_114(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TOMBOYA LC - TOM MBOYA LABOUR COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TOMBOYA-LC")
def TOMBOYA():
    return render_template("campus/TOMBOYA LC.html")

# TOTAL TVC
@app.route('/course_automating_folder_creating/TOTAL TVC - TOTAL TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_115(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TOTAL TVC - TOTAL TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TOTAL-TVC")
def TOTAL_TVC():
    return render_template("campus/TOTAL TVC.html")

# TRUC
@app.route('/course_automating_folder_creating/TRUC - TURKANA UNIVERSITY COLLEGE/<course_name>')
def course_116(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TRUC - TURKANA UNIVERSITY COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TRUC")
def TRUC():
    return render_template("campus/TRUC.html")

# TSEIKURU TTI
@app.route('/course_automating_folder_creating/TSEIKURU TTI - TSEIKURU TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_117(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TSEIKURU TTI - TSEIKURU TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TSEIKURU")
def TSEIKURU():
    return render_template("campus/TSEIKURU TTI.html")

# TTU
@app.route('/course_automating_folder_creating/TTU - TAITA TAVETA UNIVERSITY/<course_name>')
def course_118(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TTU - TAITA TAVETA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TTU")
def TTU():
    return render_template("campus/TTU.html")

# TUC
@app.route('/course_automating_folder_creating/TUC - TANGAZA UNIVERSITY COLLEGE/<course_name>')
def course_119(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TUC - TANGAZA UNIVERSITY COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TUC")
def TUC():
    return render_template("campus/TUC.html")

# TUK
@app.route('/course_automating_folder_creating/TUK - TECHNICAL UNIVERSITY OF KENYA/<course_name>')
def course_120(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TUK - TECHNICAL UNIVERSITY OF KENYA/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TUK")
def TUK():
    return render_template("campus/TUK.html")

# TUM
@app.route('/course_automating_folder_creating/TUM - TECHNICAL UNIVERSITY OF MOMBASA/<course_name>')
def course_121(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TUM - TECHNICAL UNIVERSITY OF MOMBASA/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TUM")
def TUM():
    return render_template("campus/TUM.html")

# TURBO TVC
@app.route('/course_automating_folder_creating/TURBO TVC - TURBO TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_122(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TURBO TVC - TURBO TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TURBO")
def TURBO():
    return render_template("campus/TURBO.html")

# TURKANA EAST TVC
@app.route('/course_automating_folder_creating/TURKANA EAST TVC - TURKANA EAST TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_123(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TURKANA EAST TVC - TURKANA EAST TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TURKANA-EAST")
def TURKANA_EAST():
    return render_template("campus/TURKANA EAST TVC.html")

# TURKANA NORTH
@app.route('/course_automating_folder_creating/TURKANA NORTH TVC - TURKANA NORTH TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_124(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/TURKANA NORTH TVC - TURKANA NORTH TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/TURKANA-NORTH")
def TURKANA_NORTH():
    return render_template("campus/TURKANA NORTH TVC.html")

# UGENYA TVC
@app.route('/course_automating_folder_creating/UGENYA TVC - UGENYA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_125(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/UGENYA TVC - UGENYA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/UGENYA")
def UGENYA():
    return render_template("campus/UGENYA TVC.html")

# UGUNJA TVC
@app.route('/course_automating_folder_creating/UGUNJA TVC - UGUNJA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_126(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/UGUNJA TVC - UGUNJA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/UGUNJA")
def UGUNJA():
    return render_template("campus/UGUNJA TVC.html")

# UOE
@app.route('/course_automating_folder_creating/UOE - UNIVERSITY OF ELDORET/<course_name>')
def course_127(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/UOE - UNIVERSITY OF ELDORET/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/UOE")
def UOE():
    return render_template("campus/UOE.html")

# UOEM TI
@app.route('/course_automating_folder_creating/UOEM TI - THE UNIVERSITY OF EMBU TVET INSTITUTE/<course_name>')
def course_128(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/UOEM TI - THE UNIVERSITY OF EMBU TVET INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/UOEM-TI")
def UOEM_TI():
    return render_template("campus/UOEM TI.html")

# UOEM
@app.route('/course_automating_folder_creating/UOEM - UNIVERSITY OF EMBU/<course_name>')
def course_129(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/UOEM - UNIVERSITY OF EMBU/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/UOEM")
def UOEM():
    return render_template("campus/UOEM.html")

# UOK
@app.route('/course_automating_folder_creating/UOK - UNIVERSITY OF KABIANGA/<course_name>')
def course_130(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/UOK - UNIVERSITY OF KABIANGA/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/UOK")
def UOK():
    return render_template("campus/UOK.html")

# UON
@app.route('/course_automating_folder_creating/UON - UNIVERSITY OF NAIROBI/<course_name>')
def course_131(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/UON - UNIVERSITY OF NAIROBI/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/UON")
def UON():
    return render_template("campus/UON.html")

# URIRI TVC
@app.route('/course_automating_folder_creating/URIRI TVC - URIRI TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_132(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/URIRI TVC - URIRI TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/URIRI")
def URIRI():
    return render_template("campus/URIRI TVC.html")

# UZIMA
@app.route('/course_automating_folder_creating/UZIMA - UZIMA UNIVERSITY/<course_name>')
def course_133(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/UZIMA - UZIMA UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/UZIMA")
def UZIMA():
    return render_template("campus/UZIMA.html")

# WAJIR EAST TVC
@app.route('/course_automating_folder_creating/WAJIR EAST TVC - WAJIR EAST TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_134(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/WAJIR EAST TVC - WAJIR EAST TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/WAJIR-EAST")
def WAJIR_EAST():
    return render_template("campus/WAJIR EAST TVC.html")

# WANGA TVC
@app.route('/course_automating_folder_creating/WANGA TVC - WANGA TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_135(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/WANGA TVC - WANGA TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/WANGA")
def WANGA():
    return render_template("campus/WANGA TVC.html")

# WEBUYE WEST TVC
@app.route('/course_automating_folder_creating/WEBUYE WEST TVC - WEBUYE WEST TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_136(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/WEBUYE WEST TVC - WEBUYE WEST TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/WEBUYE-WEST")
def WEBUYE_WEST():
    return render_template("campus/WEBUYE WEST TVC.html")

# WERU TVC
@app.route('/course_automating_folder_creating/WERU TVC - WERU TECHNICAL AND VOCATIONAL COLLEGE/<course_name>')
def course_137(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/WERU TVC - WERU TECHNICAL AND VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/WERU")
def WERU():
    return render_template("campus/WERU TVC.html")

# WOTE TTI
@app.route('/course_automating_folder_creating/WOTE TTI - WOTE TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_138(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/WOTE TTI - WOTE TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/WOTE")
def WOTE():
    return render_template("campus/WOTE TTI.html")

# WUMINGU TVC
@app.route('/course_automating_folder_creating/WUMINGU TVC - WUMINGU TECHNICAL & VOCATIONAL COLLEGE/<course_name>')
def course_140(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/WUMINGU TVC - WUMINGU TECHNICAL & VOCATIONAL COLLEGE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/WUMINGU")
def WUMINGU():
    return render_template("campus/WUMINGU TVC.html")

# ZETECH
@app.route('/course_automating_folder_creating/ZETECH - ZETECH UNIVERSITY/<course_name>')
def course_141(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/ZETECH - ZETECH UNIVERSITY/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/ZETECH")
def ZETECH():
    return render_template("campus/ZETECH.html")

# ZIWA
@app.route('/course_automating_folder_creating/ZIWA TTI - ZIWA TECHNICAL TRAINING INSTITUTE/<course_name>')
def course_142(course_name):
    sanitized_name = sanitize_course_name(course_name)
    template_path = f'course_automating_folder_creating/ZIWA TTI - ZIWA TECHNICAL TRAINING INSTITUTE/{sanitized_name}.html'
    try:
        return render_template(template_path)
    except Exception as e:
        print(f"Error: {e}")
        abort(404)

@app.route("/ZIWA")
def ZIWA():
    return render_template("campus/ZIWA TTI.html")