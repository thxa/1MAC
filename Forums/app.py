from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def root():
    return home()


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/SayHello/<name>")
def say_hello(name):
    return "Hello %s" % name


app.run()
