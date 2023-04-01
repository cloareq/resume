from flask import Flask, render_template, request, redirect, url_for
import json
from pathlib import Path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user data from form
        personal_info = {
            'name': request.form.get('name'),
            'surname': request.form.get('surname'),
            'location': request.form.get('location'),
            'email': request.form.get('email'),
            'website': request.form.get('website'),
        }

        # Save user data and redirect to resume page
        return redirect(url_for('resume', **personal_info))
    return render_template('index.html')

@app.route('/build_resume', methods=['POST'])
def build_resume():
    data = {
        'profile': {
            'name': request.form.get('name'),
            'surname': request.form.get('surname'),
            'location': request.form.get('location'),
            'email': request.form.get('email'),
            'website': request.form.get('website'),
        },
        'education': {
            'school_name': request.form.get('school_name'),
            'school_location': request.form.get('school_location'),
            'degree': request.form.get('degree'),
            'major': request.form.get('major'),
            'gpa': request.form.get('gpa'),
            'start_date': request.form.get('start_date'),
            'end_date': request.form.get('end_date'),
        }
    }
    
    # Save data to a JSON file
    json_file_path = Path('resumes') / f"{data['profile']['name']}_{data['profile']['surname']}.json"
    json_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    return f"Resume saved as {json_file_path.name}"



if __name__ == '__main__':
    app.run(debug=True)
