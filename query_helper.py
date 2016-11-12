#!/usr/bin/env python
from flask import *
import MySQLdb

# This file just contains the helper methods built to make routing simple

# call the db on a query with authentication
def build_response_auth(function, *args):
    if validate():
        return build_response(function, *args)
    else:
        abort(403)

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

# admittedly, this is a stupid way to do this and very unmaintainable #YOLO
def scrape_json(table_name):
    json = request.get_json(silent=True)
    ret = [] #array to return
    dic = []
    if table_name == 'comic':
        dic = comic 
    elif table_name == 'publisher':
        dic = publisher
    elif table_name == 'writer':
        dic = writer
    elif table_name == 'series':
        dic = series
    else:
        abort(400)
    
    for key in dic:
        val = json.get(key, 'NULL')
        if not val.isdigit() and val != 'NULL':
            val = "\"" + val + "\""
        ret.append(val)
    return ", ".join(ret)

## DICTIONARY FOR JSON PARSING ##
comic = ['series_id', 'issue_number', 'grade', 'image_url', 'writer_id', 'user_id', 'month', 'year',]
publisher = ['name']
series = ['name', 'first_issue', 'last_issue', 'start_year', 'end_year', 'publisher_id']
writer = ['first_name', 'last_name']

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
