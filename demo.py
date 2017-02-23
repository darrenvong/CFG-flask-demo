# To use functions from a library you installed via pip, you have to import them first.
# Importing functions using the "from x import a, b, c" style allows you to use
# the function directly as if *you* had written the code yourself.
from flask import Flask, render_template, request

# This creates the all important Flask application which will give us the ability
# to serve (respond) web pages back to our users based on the web address they
# typed in the browser
app = Flask("demo")

"""The @app.route(...) lines before the following functions are what's known as
"decorators". The basic concept you need to know here is that they "decorate"
the standard functions so that they can respond to users who will be using
the application through a browser."""

# This will return the sentence "Hello Code First Girls" to the user's browser who
# visit the root path of your website. (most likely "localhost" since you will be
# developing this application locally on your computer first)
@app.route("/")
def hello():
    return "Hello Code First Girls"

# <name> is a placeholder which holds the value of whatever a user has typed in
# after "localhost". The placeholder is what gives the flexibility that allows this
# hello string to address to someone accordingly depending on what they typed in
# the address in their browser
@app.route("/<name>")
def hello_someone(name):
    return "Hello {0}!".format(name)

# For more complicated applications, it is easier to display pages through HTML,
# a language which is used to layout the pages you see by your browser. Flask has
# added another layer on top which allows your application to feed dynamic contents
# to your HTML through the use of "templates"
@app.route("/bye/<name>")
def bye_someone(name):
    # In order for the templates we are using to have access to the dynamic data
    # processed in Python/Flask, we need to pass these as additional variables
    # after the name of the template. In this example, the name the user has
    # typed in the web address will be made available to the template via the
    # variable called "name"
    return render_template("hello.html", bye=True, name=name.title())

@app.route("/goodbye/<name>/<time>")
def bye_custom(name, time):
    return render_template("hello.html", bye=True, name=name.title(), time=time)


# Normally, when you are typing in a web address to visit a website, you are doing
# so under a method known as a "get request". However, when you need to give users
# the ability to send data through a form (e.g. when you are sending in your name
# and password to log in to the university's website), this is done via a different
# "method" known as a "post request".
#
# In order for your functions to be able to respond to a "post request", in addition
# to a normal "get request", you need to declare it after the name of the path
# you want your page and your form to respond to in app.route(...) as shown below
@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET': # the request comes from a normal browser visit to the website
        return render_template("feedback.html")
    else: # the request is send from a form you have set up in the HTML of your page
        return render_template("form_response.html", form_data=request.form)

# Passing in "debug=True" to app.run(...) will make your Flask powered server/
# application automatically refreshes upon any changes you make to this file.
app.run(debug=True)
