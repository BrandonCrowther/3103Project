#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# xxxxx= last 5 digits of your studentid. If xxxxx > 65535, subtract 30000
if __name__ == "__main__":
    app.run(host="info3103.cs.unb.ca", port=xxxx, debug=True)
