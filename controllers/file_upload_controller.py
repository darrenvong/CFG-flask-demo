"""
This controller module consists of functions responsible for
orchestrating the functionalities for the 'File Upload' page on the server-side.

@author: Darren
"""

from werkzeug.utils import secure_filename

WHITE_LIST_PARAMS = set(["name", "file_input"])

def upload_file_to_server(file_):
    secured_name = secure_filename(file_.filename)
    file_.save(secured_name)
