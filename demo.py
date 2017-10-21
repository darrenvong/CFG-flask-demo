from secrets import token_urlsafe

from flask import Flask, abort, render_template, request, session, redirect

from helper import is_valid_form_submission
from controllers.file_upload_controller import upload_file_to_server, \
    WHITE_LIST_PARAMS as file_upload_params
from controllers.twitter_demo_controller import request_access_token, \
    get_access_token

app = Flask("demo")
session = {}

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
    feedback_params = set(["email", "name", "comments"])
    if not is_valid_form_submission(request.form.keys(), feedback_params):
        # better error handling to custom error page if I have time to do so...
        abort(400)
    return render_template("comment_ok.htm.j2", name=request.form["name"],
                           comments=request.form["comments"])

@app.route("/file_upload", methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        if not (is_valid_form_submission(request.form.keys(), file_upload_params) or
                is_valid_form_submission(request.files.keys(), file_upload_params)):
            abort(400)

        upload_file_to_server(request.files['file_input'])

        return render_template("file_ok.htm.j2", name=request.form["name"])
    # it must be a GET request since that's the only other allowed request on this path
    else:
        return render_template("file_upload.htm.j2")

@app.route("/twitter")
def twitter_example():
    return render_template("twitter.htm.j2")

@app.route("/twitter_search", methods=["POST"])
def twitter_search_handler():
    session["s"] = request.form["s"]
    return redirect(request_access_token(session))

@app.route("/twitter_search_cb")
def twitter_search_cb():
    verifier = request.args.get("oauth_verifier")
    resp_text = get_access_token(verifier, session)
    print("Access Token: " + session["access_token"])
    print("Access Token Secret: " + session["access_token_secret"])
    return resp_text

# A Pythonic convention which allows you import this script without necessarily
# running the flask app defined here
if __name__ == "__main__":
    app.run(debug=True)
