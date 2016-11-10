#!/usr/bin/env python
from flask import *
import MySQLdb

# This file just contains the helper methods built to make routing simple

# call the db on a query with authentication
def build_response_auth(function, *args):
    return validate(build_response(function, *args)

# without
def build_response(function, *args):
    return call_db(make_query(function, *args)) + "\n"

# build query string and call the db using a specified function
def make_query(function, *args):
    args = list(args)
    for n,x in enumerate(args):
        args[n] = str(x)
    sql = "call " + function + "(" + ', '.join(args) + ");"
    return sql

# call db with sql string and return results
def call_db(sql_string):
    connection = MySQLdb.connect(host='localhost', user='bcrowthe', passwd='Mu7YlQr2', db='bcrowthe')
    try:
        cursor = connection.cursor()
        cursor.execute(sql_string)
        return str(cursor.fetchone())
    except Exception, e:
        print e
    return "ERROR IN SQL STATEMENT: " + sql_string
    abort(400)

# quickly validate and call the method passed to it
# sidenote, I wish there was a way to force validation using decorators
def validate():
    if 'username' in session:
        return True
    else:
        abort(403)
