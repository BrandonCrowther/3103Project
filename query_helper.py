#!/usr/bin/env python
from flask import make_response
import MySQLdb

# This file just contains the helper methods built to make routing simple

# call the db on a query
def build_response(function, *args):
    return make_response(call_db(make_query(function, *args)) + "\n", 200)

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
