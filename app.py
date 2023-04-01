from flask import Flask, render_template, request, make_response
import json
import os
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/build_resume', methods=['POST'])
def build_resume():
    data = {
        'name': request.form['name'],
        'surname': request.form['surname'],
        'location': request.form['location'],
        'email': request.form['email'],
        'website': request.form['website'],
        'education': get_education_data(request.form),
        'experience': get_experience_data(request.form)
    }

    save_resume_data(data)

    # Convert the resume data to a PDF
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in'
    }

    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    resume_html = render_template('resume.html', data=data)
    resume_pdf = pdfkit.from_string(resume_html, False, options=options, configuration=config)
    # Offer the PDF as a download
    response = make_response(resume_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=resume.pdf'

    return response



def get_education_data(form):
    school_names = form.getlist('school_name[]')
    school_locations = form.getlist('school_location[]')
    degrees = form.getlist('degree[]')
    majors = form.getlist('major[]')
    gpas = form.getlist('gpa[]')
    start_dates = form.getlist('start_date[]')
    end_dates = form.getlist('end_date[]')

    education_data = []
    for i in range(len(school_names)):
        education = {
            'school_name': school_names[i],
            'school_location': school_locations[i],
            'degree': degrees[i],
            'major': majors[i],
            'gpa': gpas[i],
            'start_date': start_dates[i],
            'end_date': end_dates[i]
        }
        education_data.append(education)

    return education_data

def get_experience_data(form):
    company_names = form.getlist('company_name[]')
    job_titles = form.getlist('job_title[]')
    job_locations = form.getlist('job_location[]')
    start_dates = form.getlist('start_date[]')
    end_dates = form.getlist('end_date[]')
    job_responsibilities = form.getlist('job_responsibilities[]')

    experience_data = []
    for i in range(len(company_names)):
        experience = {
            'company_name': company_names[i],
            'job_title': job_titles[i],
            'job_location': job_locations[i],
            'start_date': start_dates[i],
            'end_date': end_dates[i],
            'job_responsibilities': job_responsibilities[i]
        }
        experience_data.append(experience)

    return experience_data


def save_resume_data(data):
    # Create the resumes folder if it doesn't exist
    if not os.path.exists('resumes'):
        os.makedirs('resumes')

    filename = f"{data['name'].lower()}_{data['surname'].lower()}.json"
    filepath = os.path.join('resumes', filename)

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
