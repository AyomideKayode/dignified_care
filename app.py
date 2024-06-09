#!/usr/bin/env python3

"""
Flask app to handle contact form submissions.
"""

from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Use environment variables for sensitive information
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'], strict_slashes=False)
def submit_form():
    try:
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')

        # Log received form data
        print(
            f"Received form data - Name: {name}, Phone: {phone}, Email: {email}, Message: {message}")

        # Create the email content
        email_content = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        # Create a MIMEText object with the email content
        msg = MIMEText(email_content)
        # Set the subject of the email
        msg['Subject'] = 'Dignified Care New Contact Form Submission'
        # Set the sender of the email
        msg['From'] = f"{name} <{email}>"
        # Set the recipient of the email
        msg['To'] = 'admin@dignifiedcare.uk'

        # Send the email
        try:
            # Create an SMTP server object with the Gmail SMTP
            #  server address and port number
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                # Start a secure TLS connection
                server.starttls()
                # Login to the email account using the provided
                # email address and password
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                # Send the email message
                server.send_message(msg)
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
