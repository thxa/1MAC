from flask import Flask

app = Flask("__name__")


@app.route("/index")
def home():
    return "Hi there"


@app.route("/SayHello/<name>")
def hello_name(name):
    return "Hello %s" % name


app.run()
