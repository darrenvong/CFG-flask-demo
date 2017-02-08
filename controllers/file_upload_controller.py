"""
This controller module consists of functions responsible for
orchestrating the functionalities for the 'File Upload' page on the server-side.

@author: Darren
"""
import os

import requests
from werkzeug.utils import secure_filename

from helper import EmailNotSentException, DOMAIN_NAME, ADMIN_EMAIL, API_KEY

WHITE_LIST_PARAMS = set(["name", "file_input"])

def send_email_with_file(name, file_):
    # Inline style only done as a demo. Not recommended in general for larger HTML pages!
    html_message = """
    <h3>Hi Darren, </h3>
    
    <p style='color:red;'>{0} has sent you the following file via your upload form.</p>
    """.format(name)
    secured_name = secure_filename(file_.filename)
    file_.save(secured_name)
    send_response = requests.post(
        "https://api.mailgun.net/v3/{0}/messages".format(DOMAIN_NAME),
        auth=("api", API_KEY),
        files=[("attachment", open(secured_name, "rb"))],
        data={"from": "demo@{0}".format(DOMAIN_NAME),
              "to": ADMIN_EMAIL,
              "subject": "A fan has sent you a file",
              "html": html_message
        }
    )
    
    if send_response.status_code == 200:
        print "HTML styled email successfully sent with file"
    else:
        print send_response.status_code
        raise EmailNotSentException("Failed to send email (API error)")
    os.remove(secured_name)
    