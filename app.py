#!/usr/bin/env python3

"""
Flask app to handle contact form submissions.
"""

from flask import Flask, request, jsonify, render_template, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Use environment variables for sensitive information
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Home page route.
    """
    return render_template('index.html')


@app.route('/recruitment', methods=['GET'], strict_slashes=False)
def recruitment():
    """ Recruitment page route.
    """
    return render_template('recruitment.html')


@app.route('/submit', methods=['POST'], strict_slashes=False)
def submit_form():
    """Handle form submission.

    Function that processes the form data submitted by the user.
    Retrieves the form data, saves any uploaded files,
    creates an email with the form data as the content,
    attaches any uploaded files to the email, and sends the email.

    Returns:
        A JSON response indicating the status of the form submission.
        If the email is sent successfully, the response
        will have a status of "success" and a HTTP status code of 200.
        If there is an error during the form submission process,
        the response will have a status of "error" and a HTTP status code of 500.

    Raises:
        SMTPException:
            If there is an error with the SMTP server while sending the email.
        Exception:
            If there is a general error during the form submission process.
    """
    try:
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')

        # Log received form data
        print(
            f"Received form data - Name: {name}, Phone: {phone}, Email: {email}, Message: {message}")

        # save uploaded files
        cv = request.files['cv']
        recommendation = request.files['recommendation']

        attachments = []
        if cv:
            cv_path = os.path.join(app.config['UPLOAD_FOLDER'], cv.filename)
            cv.save(cv_path)
            attachments.append(cv_path)  # Save CV file path to attachments list

        if recommendation:
            rec_path = os.path.join(app.config['UPLOAD_FOLDER'], recommendation.filename)
            recommendation.save(rec_path)
            # Save recommendation file path to attachments list
            attachments.append(rec_path)

        # Create the email content
        email_content = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        # msg = MIMEText(email_content)
        # Create a MIMEMultipart object to handle multiple parts of the email
        msg = MIMEMultipart()
        msg.attach(MIMEText(email_content))

        # attach files to email
        for file_path in attachments:
            with open(file_path, 'rb') as file:
                # Create a MIMEApplication object to represent the file
                part = MIMEApplication(file.read(), Name=os.path.basename(file_path))
                # Add the file as an attachment to the email
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                msg.attach(part)  # Attach the file to the email

        # Set the subject of the email
        msg['Subject'] = 'Dignified Care New Contact Form Submission'
        # Set the sender of the email
        msg['From'] = f"{name} <{email}>"
        # Set the recipient of the email
        msg['To'] = 'admin@dignifiedcare.uk'

        # Send the email
        try:
            # Create an SMTP server object with the Gmail SMTP
            # server address and port number
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()  # Start a secure TLS connection
                # Login to the email account using the provided
                # email address and password
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)  # Send the email message
            # Return a success response if the email is sent successfully
            return jsonify({"status": "success"}), 200
        except smtplib.SMTPException as e:
            # Handle SMTP errors and return an error response
            print(f"SMTP error: {e}")
            return jsonify({"status": "error", "message": f"SMTP error: {e}"}), 500
        except Exception as e:
            # Handle general errors and return an error response
            print(f"General error: {e}")
            return jsonify({"status": "error", "message": f"General error: {e}"}), 500

    except Exception as e:
        print(f"Failed to process form data: {e}")
        return jsonify(
            {"status": "error", "message":
             f"Form data processing error: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
