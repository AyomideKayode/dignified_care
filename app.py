#!/usr/bin/env python3

"""
Flask app to handle contact form submissions.
"""

from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
import os

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
        email = request.form.get('email')
        message = request.form.get('message')

        print(
            f"Received form data - Name: {name}, Email: {email}, Message: {message}")

        # Create the email content
        email_content = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg = MIMEText(email_content)
        msg['Subject'] = 'New Contact Form Submission'
        msg['From'] = f"{name} <{email}>"
        msg['To'] = 'kazzywiz7@gmail.com'

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
            return jsonify({"status": "success"}), 200
        except smtplib.SMTPException as e:
            print(f"SMTP error: {e}")
            return jsonify(
                {"status": "error", "message": f"SMTP error: {e}"}), 500
        except Exception as e:
            print(f"General error: {e}")
            return jsonify(
                {"status": "error", "message": f"General error: {e}"}), 500

    except Exception as e:
        print(f"Failed to process form data: {e}")
        return jsonify(
            {"status": "error", "message": f"Form data processing error: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
