// main.js
// This file contains the JavaScript code for the website.

document
  .getElementById('contact-form')
  .addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    fetch('/submit', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === 'success') {
          alert('Thank you for contacting us!');
        } else {
          alert('There was an error. Please try again.');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        alert('There was an error. Please try again.');
      });
  });
