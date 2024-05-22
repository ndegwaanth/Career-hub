from flask import Flask, render_template
import json

app = Flask(__name__)

# Function to load JSON data from file
def load_institutions_data():
    with open('institutions.json') as json_file:
        return json.load(json_file)

@app.route('/')
def index():
    institutions_data = load_institutions_data()
    return render_template('index.html', institutions=institutions_data['institutions'])

if __name__ == '__main__':
    app.run(debug=True)