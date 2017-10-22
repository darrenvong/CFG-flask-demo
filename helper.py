"""
A module consists of a collection of helper functions/classes that are useful for
the whole application.

@author: Darren
"""

def is_valid_form_submission(sent_params, allowed_params):
    """Basic paramaters validation to prevent form hacking. Returns True
    if parameters submitted from form by user are those allowed, False otherwise.
    """
    for sent in sent_params:
        if sent not in allowed_params:
            return False
    return True
