#!/usr/bin/env python
from flask import Flask, make_response
import math
import MySQLdb

app = Flask(__name__)
@app.route("/")
def start():
    return "COMIC SERVICE INITIATED\n"


# Comics
@app.route("/comics/")
def get_collection():
    return build_response("get_comics")

@app.route("/comics/<int:comic_id>")
def get_collection(comic_id):
    return build_response("get_comic", comic_id)

# get all issues owned by the user in a series
@app.route("/comics/series/<int:series_id>")
def get_issues_from_series(series_id):
    return build_response("get_issues_from_series", series_id)

@app.errorhandler(404)
def not_found(error):
    return make_response("<p>Say what?</p>\n", 404)

####################
## HELPER METHODS ##
####################

# call the db on a query
def build_response(function, *args)):
    return make_response(call_db(make_query(function, *args))) + "\n"

# build query string and call the db using a specified function
def make_query(function, *args):
    args = list(args)
    for n,x in enumerate(args):
        args[n] = str(x)
    sql = "call " + function + "(" + ', '.join(args) + ");"
    return sql

# call db with sql string and return results
def call_db(sql_string):
    # Make the connection
    connection = MySQLdb.connect(host='localhost',user='bcrowthe',passwd='Mu7YlQr2',db='bcrowthe')

    # Run query and get result
    try:
        cursor = connection.cursor()
        cursor.execute(sql_string)
        return str(cursor.fetchone())
    except Exception, e:
        print e
    return "ERROR IN SQL STATEMENT: " + sql_string


# xxxxx= last 5 digits of your studentid. If xxxxx > 65535, subtract 30000
if __name__ == "__main__":
    app.run(host="info3103.cs.unb.ca", port=43005, debug=True)
