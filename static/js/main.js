function showSection(sectionId) {
    const sections = ['profile-section', 'education-section', 'experience-section'];
    for (const section of sections) {
        const element = document.getElementById(section);
        if (sectionId === section) {
            element.style.display = '';
        } else {
            element.style.display = 'none';
        }
    }
}

function addSchool() {
    const schoolFields = document.getElementById('school-fields');
    const newFields = schoolFields.cloneNode(true);
    const hr = document.createElement('hr');
    const educationSection = document.getElementById('education-section');

    // Check if there are any schools already added
    const schools = educationSection.querySelectorAll('#school-fields');
    if (schools.length > 0) {
        educationSection.appendChild(hr);
    }

    newFields.querySelectorAll('input').forEach(input => input.value = ''); // clear input values

    educationSection.appendChild(newFields);

    // Add a "Remove School" button next to the new school form
    if (schools.length > 0) {
        const removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.innerText = 'Remove School';
        removeButton.onclick = function() {
            // Remove the school form and the "Remove School" button
            educationSection.removeChild(hr);
            educationSection.removeChild(newFields);
            educationSection.removeChild(removeButton);
        };
        educationSection.appendChild(removeButton);
    }

    educationSection.appendChild(document.getElementById('add-school-button-container'));
}

function addExperience() {
    const experienceFields = document.getElementById('experience-fields');
    const newFields = experienceFields.cloneNode(true);
    const hr = document.createElement('hr');
    const experienceSection = document.getElementById('experience-section');

    // Check if there are any experiences already added
    const experiences = experienceSection.querySelectorAll('#experience-fields');
    if (experiences.length > 0) {
        experienceSection.appendChild(hr);
    }

    // Clear input values
    newFields.querySelectorAll('input').forEach(input => input.value = '');

    // Clear textarea values
    newFields.querySelectorAll('textarea').forEach(textarea => textarea.value = '');

    experienceSection.appendChild(newFields);

    // Add a "Remove Experience" button next to the new experience form
    if (experiences.length > 0) {
        const removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.innerText = 'Remove Experience';
        removeButton.onclick = function() {
            // Remove the experience form and the "Remove Experience" button
            experienceSection.removeChild(hr);
            experienceSection.removeChild(newFields);
            experienceSection.removeChild(removeButton);
        };
        experienceSection.appendChild(removeButton);
    }

    experienceSection.appendChild(document.getElementById('add-experience-button-container'));
}

function buildResume() {
    const formData = new FormData(document.getElementById('resume-form'));

    fetch('/build_resume', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'resume.pdf';
        document.body.appendChild(a);
        a.click();
        a.remove();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

