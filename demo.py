import os

from flask import Flask, abort, render_template, request
import requests

# Accessing API keys and confidential information stored in environment variables
# (for security reasons. Alternatively, store them in a secret configuration file.
# Whatever option you choose, do not push these to GitHub!
API_KEY = os.environ['MAILGUN_API_KEY']
DOMAIN_NAME = os.environ['MAILGUN_DOMAIN_NAME']
ADMIN_EMAIL = os.environ['MAILGUN_ADMIN_EMAIL']

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

class EmailNotSentException(Exception):
    def __init__(self, message):
        super(EmailNotSentException, self).__init__(message)
        
    def __str__(self, *args, **kwargs):
        return "EmailNotSentException: {}".format(self.message)

def send_email(name, comment, email):
    send_response = requests.post(
        "https://api.mailgun.net/v3/{0}/messages".format(DOMAIN_NAME),
        auth=("api", API_KEY),
        data={"from": "CF:G Demo <demo@{0}>".format(DOMAIN_NAME),
              "to": ADMIN_EMAIL,
              "subject": "Someone has commented on your site!",
              "text": """
              Hi Darren,
              
              {0} ({2}) has posted the following comment on your website:
              {1}
              """.format(name, comment, email)})
    # A response code of 200 means the request to send the email succeeded
    if send_response.status_code == 200:
        print "Email successfully sent"
    else:
        print send_response.status_code
        raise EmailNotSentException("Failed to send email (API error)")

@app.route("/feedback_submit", methods=['POST'])
def sign_up():
    # Basic paramaters validation to prevent form hacking
    white_list_params = set(['email', 'comments', 'name'])
    for param in request.form.iterkeys():
        if param not in white_list_params:
            abort(400)
    print "Sending the following response..."
    try:
        send_email(request.form['name'], request.form['comments'],
            request.form['email'])
    except EmailNotSentException as e:
        print e.message
        abort(400)
    
    return render_template("ok.htm.j2")

# A Pythonic convention which allows you import this script without necessarily
# running the flask app defined here
if __name__ == "__main__":
    app.run(port=80, debug=True)
