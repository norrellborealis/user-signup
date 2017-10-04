from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    error_check = False
    username_err = ''
    password_err = ''
    verify_password_error = ''
    email_err = ''

    if " " in username or username == '':
        username_err = "Not a valid username."
        error_check = True
    elif len(username) < 3 or len(username) > 20:
        username_err = "Username is not a valid length."
        error_check = True
    if ' ' in password or password == '':
        password_err = "Not a valid password."
        password = ''
        verify_password = ''
        error_check = True
    elif len(password) < 3 or len(password) > 20:
        password_err = "Password is not a valid length."
        password = ''
        verify_password = ''
        error_check = True
    if password != verify_password:
        verify_password_error = "Passwords do not match."
        password = ''
        verify_password = ''
        error_check = True
    elif verify_password == '':
        verify_password_error = "Passwords do not match."
        error_check = True
    
    if email != '':
        if email.count('@') != 1:
            email_err = "Not a valid email address."
            error_check = True
        if email.count('.') != 1:
            email_err = "Not a valid email address."
            error_check = True
        if " " in email:
            email_err = "Not a valid email address."
            error_check = True
    if error_check == True:
        return render_template('index.html', username_err=username_err,
            password_err=password_err, verify_password_error=verify_password_error,
            email_err=email_err, username=username, password=password,
            verify_password=verify_password, email=email)
    else:
        return render_template('welcome_page.html', username=username)
app.run()