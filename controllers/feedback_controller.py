"""
This controller module consists of functions responsible for
orchestrating the functionalities for the 'Feedback' page on the server-side.

@author: Darren
"""
import os

import requests

from helper import EmailNotSentException, DOMAIN_NAME, ADMIN_EMAIL, API_KEY

WHITE_LIST_PARAMS = set(["email", "name", "comments"])

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
