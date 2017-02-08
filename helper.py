"""
A module consists of a collection of helper functions/classes that are useful for
the whole application.

@author: Darren
"""
import os

# Accessing API keys and confidential information stored in environment variables
# (for security reasons. Alternatively, store them in a secret configuration file.
# Whatever option you choose, do not push these to GitHub!
API_KEY = os.environ['MAILGUN_API_KEY']
DOMAIN_NAME = os.environ['MAILGUN_DOMAIN_NAME']
ADMIN_EMAIL = os.environ['MAILGUN_ADMIN_EMAIL']

class EmailNotSentException(Exception):
    def __init__(self, message):
        super(EmailNotSentException, self).__init__(message)
        
    def __str__(self, *args, **kwargs):
        return "EmailNotSentException: {}".format(self.message)


def is_valid_form_submission(sent_params, allowed_params):
    """Basic paramaters validation to prevent form hacking. Returns True
    if parameters submitted from form by user are those allowed, False otherwise.
    """
    for sent in sent_params:
        if sent not in allowed_params:
            return False
    return True
        