import os

from flask import Flask, abort, render_template, request
import requests

app = Flask("demo")

@app.errorhandler(400)
def display_400(error):
    return render_template("400.htm.j2")

@app.route("/")
def hello():
    print __name__
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

# A Pythonic convention which allows you import this script without necessarily
# running the flask app defined here
if __name__ == "__main__":
    app.run(port=80, debug=True)
