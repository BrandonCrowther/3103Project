#!/usr/bin/env python
from flask import Flask, make_response
import math

app = Flask(__name__)
@app.route("/")
def start():
    return "I love Python!\n"

@app.route("/user/<name>")
def hello(name):
    return "Well, hello <strong> %s"  % name +"!</strong></br>\n"

@app.route("/user/<name>/<int:value>")
def squareRoot(name, value):
    return "Thanks %s"  % name + " The square root of %f" % value + " is %f" % math.sqrt(value) + "\n"


@app.errorhandler(404)
def not_found(error):
    return make_response("<p>Say what?</p>\n", 404)

# xxxxx= last 5 digits of your studentid. If xxxxx > 65535, subtract 30000
if __name__ == "__main__":
    app.run(host="info3103.cs.unb.ca", port=xxxx, debug=True)
