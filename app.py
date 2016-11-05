#!/usr/bin/env python
import sys
from flask import Flask
from query_helper import *
from flask_restful import reqparse, Resource, Api
from flask_session import Session
from settings import *
import math

## Boiler Plate Code ##
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
# Set Server-side session config: Save sessions in the local app directory.
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = COOKIES_SESSION_TYPE
app.config['SESSION_COOKIE_NAME'] = COOKIES_SESSION_HOST
app.config['SESSION_COOKIE_DOMAIN'] = APP_HOST
Session(app)

## Routing ##
@app.route("/")
def start():
    return "Wow this is the default directory!\n"

# Comics
@app.route("/comics/")
def get_comics():
    return build_response("get_comics")

@app.route("/comics/<int:comic_id>")
def get_comic(comic_id):
    return build_response("get_comic", comic_id)

@app.route("/comics/series/<int:series_id>")
def get_issues_from_series(series_id):
    return build_response("get_issues_from_series", series_id)

@app.route("/comics/publisher/<int:publisher_id>")
def get_issues_from_publisher(publisher_id):
    return build_response("get_issues_from_publisher", publisher_id)

@app.route("/comics/writer/<int:writer_id>")
def get_issues_from_writer(writer_id):
    return build_response("get_issues_from_writer", writer_id)

@app.errorhandler(404)
def not_found(error):
    return make_response("404 Not Found\n", 404)

# xxxxx= last 5 digits of your studentid. If xxxxx > 65535, subtract 30000
if __name__ == "__main__":
    app.run(host = APP_HOST, port = APP_PORT, debug = APP_DEBUG)
