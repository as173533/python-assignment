# Flask Registration Form

This is a small Flask project for a registration form assignment.

## Project Structure

- `register.py` - main Flask app for the registration form
- `templates/register.html` - registration form page
- `templates/register_confirm.html` - confirmation page after the form is submitted
- `templates/base.html` - simple base template used by the older index page
- `hyperlink.py` - earlier practice app for links and images
- `static/demo.jpg` - image used by the practice app
- `screenshots/` - screenshots showing the app running

## How to Run

1. Open a terminal in this project folder.
2. Install Flask if it is not installed:

```bash
pip install -r requirements.txt
```

3. Run the registration app:

```bash
python register.py
```

4. Open this address in a browser:

```text
http://127.0.0.1:5000/register
```

## How to Test

1. Fill in first name, last name, email, phone number, and password.
2. Click the `Register` button.
3. The confirmation page should show all submitted values, including the password field.

## Entry Point

The correct file to run for this submission is `register.py`.
