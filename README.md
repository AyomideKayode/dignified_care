# Dignified Living Care

Welcome to the dignified_care project!

Dignified Living Care is a simple one-page website for a care program that assists individuals who cannot take care of themselves or families looking to provide better care for their loved ones. The website offers various services such as daytime and evening care, help with domestic chores, personal care, social activities, shopping, cooking, companionship, medication support, overnight care, specialist care, 24-hour live-in care, and respite care.

## Description

This project aims to provide dignified living care services to individuals in need. It focuses on promoting independence, comfort, and quality of life for our clients.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- List of care services offered.
- Contact form to allow users to submit inquiries.
- Backend functionality to send contact form submissions to an email address.

## Technologies Used

- HTML, CSS, JavaScript (Frontend)
- Flask (Backend)
- Python-dotenv (Environment Variables)
- SMTP (Email Service)
- _the below still under consideration_
- Nginx (Web Server)
- Gunicorn (WSGI HTTP Server)

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Virtual environment (optional but recommended)
- Git (optional for version control)

### Steps

#### 1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/dignified-living-care.git
cd dignified-living-care
```

#### 2. **Create a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

#### 4. **Create a .env file in the project root:**

```bash
touch .env
```

#### 5. **Add the following environment variables to the .env file:**

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

An app password is a long, randomly generated password that you provide only once instead of your regular password when signing in to an app or device that doesn't support two-step verification.

[Generate one here](https://myaccount.google.com/apppasswords)

### Usage

**Running the Application Locally:**

#### 1. **Start the Flask development server:**

```bash
python app.py
```

or with gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

Here's a breakdown of the command:

- `gunicorn`: The Gunicorn server.
- `-w 4`: This flag specifies the number of worker processes. Adjust this number based on your app’s requirements and server resources.
- `-b 0.0.0.0:8000`: This flag binds the server to all IP addresses on port 8000. Adjust the port if necessary.
- `wsgi:app`: This specifies the module and application. wsgi is the module name (i.e., wsgi.py without the .py extension), and app is the Flask application instance.

#### 2. **Open your web browser and go to:**

```arduino
http://127.0.0.1:5000
```

**Testing the Contact Form:**

Fill out the contact form on the webpage and submit it. If everything is set up correctly, you should receive an email with the form submission details.

### Deployment

### Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License
