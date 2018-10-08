from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#renders form
@app.route('/')
def index():
    return render_template('index.html')

#function validating lenght

# def is_long(entry):
#     try:
#         3 <= len(entry) <=20 or (' ' in entry) == True
#         return True
#     except:
#         return False 

#validates submissions
@app.route ('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    invalid_username_error = ''
    invalid_password_error = ''
    verify_error = ''
    email_error = ''

    #validating username
    if not(3 <= len(username) <=20) or (' ' in username) == True:
        invalid_username_error = "That's not valid username"
        username = ''

    else:
        username = username

    #validating password
    if not(3 <= len(password) <=20) or (' ' in password) == True:
        invalid_password_error = "That's not valid password"

    #validating password verification
    if password != verifypassword:
        verify_error = "Passwords don't match"


    #validating email
    if email == '':
        email_error = ''

    else:
        if not(3 <= len(email) <=20) or (' ' in email) == True or email.find("@")==-1 or email.find(".")==-1:
            email_error = "That's not a valid email"
            email = ''


    #overall validation

    if not invalid_username_error and not invalid_password_error and not verify_error and not email_error: 
        return render_template('welcome.html', username=username)

    else:
        return render_template('index.html',invalid_username_error = invalid_username_error, invalid_password_error = invalid_password_error,
        verify_error = verify_error, email_error = email_error, username = username, email = email)

app.run()
