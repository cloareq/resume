function showSection(section) {
    document.getElementById('profile-section').style.display = 'none';
    document.getElementById('education-section').style.display = 'none';
    document.getElementById(section).style.display = 'block';
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



function buildResume() {
    const formData = new FormData(document.getElementById('resume-form'));

    fetch('/build_resume', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(result => {
        alert(result);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
