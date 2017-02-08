import os

from flask import Flask, abort, render_template, request
import requests

from helper import EmailNotSentException, is_valid_form_submission
from controllers.feedback_controller import send_email, \
    WHITE_LIST_PARAMS as feedback_params
from controllers.file_upload_controller import send_email_with_file, \
    WHITE_LIST_PARAMS as file_upload_params

app = Flask("demo")

@app.errorhandler(400)
def display_400(error):
    return render_template("400.htm.j2")

@app.route("/")
def hello():
    return render_template("hello.htm.j2")

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.htm.j2", name=name.title())

@app.route("/bye/<name>")
def bye_someone(name):
    return render_template("hello.htm.j2", bye=True, name=name.title())

@app.route("/goodbye/<name>/<time>")
def bye_custom(name, time):
    return render_template("hello.htm.j2", bye=True, name=name.title(), time=time)

@app.route("/feedback")
def feedback_form():
    return render_template("feedback.htm.j2")

@app.route("/feedback_submit", methods=['POST'])
def sign_up():
    if not is_valid_form_submission(request.form.iterkeys(), feedback_params):
        # better error handling to custom error page if I have time to do so...
        abort(400)
    
    print "Sending the following response..."
    try:
        send_email(request.form['name'], request.form['comments'],
            request.form['email'])
    except EmailNotSentException as e:
        print e.message
        abort(400)
    
    return render_template("ok.htm.j2")

@app.route("/file_upload", methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        if not (is_valid_form_submission(request.form.iterkeys(), file_upload_params) or
                is_valid_form_submission(request.files.iterkeys(), file_upload_params)):
            abort(400)
        
        try:
            send_email_with_file(request.form['name'], request.files['file_input'])
        except EmailNotSentException as e:
            print e.message
            abort(400)
        
        return render_template("ok.htm.j2")
    # it must be a GET request since that's the only other allowed request on this path
    else:
        return render_template("file_upload.htm.j2")

# A Pythonic convention which allows you import this script without necessarily
# running the flask app defined here
if __name__ == "__main__":
    app.run(port=80, debug=True)
