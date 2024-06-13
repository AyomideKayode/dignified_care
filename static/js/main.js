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
      .then((response) => response.json()) // Convert the response to JSON
      .then((data) => {
        if (data.status === 'success') {
          alert('Thank you for contacting us!'); // Display success message
        } else {
          alert('There was an error. Please try again.'); // Display error message
        }
      })
      .catch((error) => {
        console.error('Error:', error); // Log the error to the console
        alert('There was an error. Please try again.'); // Display error message
      });
  });

document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('nav-menu');

  hamburger.addEventListener('click', function () {
    navMenu.classList.toggle('show');
    hamburger.classList.toggle('toggled');

    if (hamburger.classList.contains('toggled')) {
      hamburger.innerHTML = '✕';
    } else {
      hamburger.innerHTML = '☰';
    }
  });
});
