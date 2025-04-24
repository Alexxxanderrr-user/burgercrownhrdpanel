from flask import Flask, render_template_string, request, redirect, url_for
import random
import string
import os

# Set up the Flask app
app = Flask(__name__, static_url_path='/static', static_folder='static')

# Ensure the static folder exists
os.makedirs('static', exist_ok=True)

# Save the logo in the static folder
logo_path = 'static/logo.png'

# If the logo is not already in the static folder, you can copy it there manually.
# You can add your logo manually to the `static` folder or use other methods to upload it.

SUFFIXES = ["-R", "-W", "-D", "-S", "-T", "-SB", "-B"]

def generate_random_string(suffix):
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"HRD-{random_part}{suffix}".upper()  # Convert the generated string to uppercase

# Home page
@app.route('/')
def home():
    # HTML content for the home page with the Documentation button
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to the Burger Crown Human Resources Department!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background-color: #87CEEB;  /* Sky blue color */
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #333;
                font-size: 24px;
                text-align: center;
            }
            .highlight {
                color: gold; /* Gold color for "Human Resources" */
            }
            .logo {
                width: 100px;
                height: 100px;
                object-fit: cover;
                object-position: center;
                border-radius: 50%;
                margin-bottom: 20px;
            }
            .button-container {
                display: flex;
                gap: 20px;
                margin-top: 20px;
                flex-wrap: wrap; /* Allows wrapping of buttons on small screens */
                justify-content: center;
                width: 100%;
                max-width: 500px; /* Keep buttons from stretching too much on large screens */
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                margin: 10px;
                width: 200px; /* Give the buttons a fixed width for uniformity */
            }
            button:hover {
                background-color: #0056b3;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #333;
                text-align: center;
                font-weight: bold; /* Makes the footer text bold */
            }

            /* Mobile-specific styles */
            @media (max-width: 768px) {
                h1 {
                    font-size: 20px; /* Adjust heading size on mobile */
                }
                button {
                    width: 100%; /* Make buttons full width on smaller screens */
                    font-size: 14px;
                }
                .footer {
                    font-size: 12px; /* Smaller footer text on mobile */
                }
            }
        </style>
    </head>
    <body>
        <img src="{{ url_for('static', filename='logo.png') }}" alt="Burger Crown Logo" class="logo">
        <h1>Welcome to the Burger Crown <span class="highlight">Human Resources</span> Department!</h1>
        <div class="button-container">
            <button onclick="window.location.href='{{ url_for('case_ids') }}'">Case IDs</button>
            <button onclick="window.location.href='{{ url_for('documentation') }}'">Documentation</button>
        </div>
        <p class="footer">This resource was created for the Burger Crown Human Resources Department by 1_ItzAlexx, the Founder and Chairman of Burger Crown.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

# Case ID Generator page
@app.route('/case_ids', methods=['GET', 'POST'])
def case_ids():
    random_string = None
    if request.method == 'POST':
        suffix = request.form.get('suffix')
        if suffix in SUFFIXES:
            random_string = generate_random_string(suffix)

    # HTML content for the case ID generator page
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Burger Crown | Case IDs</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background-color: #87CEEB;  /* Sky blue color */
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #333;
                font-size: 24px;
                text-align: center;
            }
            form {
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 500px;
            }
            select, button {
                padding: 10px;
                margin: 10px;
                font-size: 16px;
                width: 100%;
            }
            p {
                font-size: 18px;
                font-weight: bold;
                color: #007BFF;
            }
            img.logo {
                width: 100px;
                height: 100px;
                object-fit: cover;
                object-position: center;
                border-radius: 50%;
                margin-bottom: 20px;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #333;
                text-align: center;
                font-weight: bold; /* Makes the footer text bold */
            }

            /* Mobile-specific styles */
            @media (max-width: 768px) {
                h1 {
                    font-size: 20px;
                }
                button {
                    font-size: 14px;
                }
                .footer {
                    font-size: 12px;
                }
            }

            /* Style for Generate button */
            button.generate-button {
                background-color: #007BFF;  /* Blue color */
                color: white;
                font-size: 16px;
                padding: 12px;
            }

            button.generate-button:hover {
                background-color: #0056b3;  /* Darker blue on hover */
            }
        </style>
    </head>
    <body>
        <img src="{{ url_for('static', filename='logo.png') }}" alt="Burger Crown Logo" class="logo">
        <h1>Burger Crown | Case IDs</h1>
        <form method="post">
            <label for="suffix">Choose a punishment type:</label>
            <select name="suffix" id="suffix">
                <option value="-R">Reminder</option>
                <option value="-W">Warning</option>
                <option value="-D">Demotion</option>
                <option value="-S">Suspension</option>
                <option value="-T">Termination</option>
                <option value="-SB">Staff Team Blacklisted</option>
                <option value="-B">Group Blacklist</option>
            </select>
            <button type="submit" class="generate-button">Generate</button>
        </form>
        {% if random_string %}
            <p>Generated String: <strong>{{ random_string }}</strong></p>
        {% endif %}

        <p class="footer">This resource was created for the Burger Crown Human Resources Department by 1_ItzAlexx, the Founder and Chairman of Burger Crown.</p>
    </body>
    </html>
    """
    return render_template_string(html_content, random_string=random_string, suffixes=SUFFIXES)

# Human Resources Documentation page
@app.route('/documentation')
def documentation():
    # HTML content for the Human Resources Documentation page with the logo
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Human Resources Documentation</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background-color: #87CEEB;  /* Sky blue color */
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #333;
                font-size: 24px;
                text-align: center;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #333;
                text-align: center;
                font-weight: bold; /* Makes the footer text bold */
            }
            .logo {
                width: 100px;
                height: 100px;
                object-fit: cover;
                object-position: center;
                border-radius: 50%;
                margin-bottom: 20px;
            }

            /* Mobile-specific styles */
            @media (max-width: 768px) {
                h1 {
                    font-size: 20px;
                }
                .footer {
                    font-size: 12px;
                }
            }
        </style>
    </head>
    <body>
        <img src="{{ url_for('static', filename='logo.png') }}" alt="Burger Crown Logo" class="logo">
        <h1>Human Resources Documentation</h1>
        <p>Coming Soon...</p>

        <p class="footer">This resource was created for the Burger Crown Human Resources Department by 1_ItzAlexx, the Founder and Chairman of Burger Crown.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
