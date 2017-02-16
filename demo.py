from flask import Flask, render_template

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

# A Pythonic convention which allows you import this script without necessarily
# running the flask app defined here
if __name__ == "__main__":
    
    """In class, to see the results of the application, we had to type
    'localhost:5000/[path_name]' to see the returned result in our browser.
    the extra 'port=80' saves you some keystroke and allows you to just type
    'localhost/[path_name]' as by default, 'localhost' is equivalent to
    'localhost:80' in browsers.
    """
    app.run(port=80, debug=True)
