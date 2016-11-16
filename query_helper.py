#!/usr/bin/env python
from flask import *
import MySQLdb
from settings import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# This file just contains the helper methods built to make routing simple

# call the db on a query with authentication
def build_response_auth(function, *args):
    if validate():
        return build_response(function, *args)
    else:
        abort(403)

# without
def build_response(function, *args):
    return call_db(function, *args)

# build query string and call the db using a specified function
def sanitize_query(*args):
    return [s.encode('utf-8') for s in args]

# admittedly, this is a stupid way to do this and very unmaintainable #YOLO
def scrape_json(table_name, comics=False):
    json = request.get_json(silent=True)
    if not json:
        abort(400)
    if comics:
        json['user_id'] = session['username']

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
        print "Could not understand dictionary " + dic
        abort(400)
    for key in dic:
        val = json.get(key, 'NULL')
        ret.append(val)
    return ret

## DICTIONARY FOR JSON PARSING ##
comic = ['issue_number', 'series_id', 'grade', 'image_url', 'writer_id', 'user_id', 'month', 'year']
publisher = ['name']
series = ['name', 'first_issue', 'last_issue', 'start_year', 'end_year', 'publisher_id']
writer = ['first_name', 'last_name']

# call db with sql string and return results
def call_db(proc, *args):
    connection = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB, use_unicode=True, charset='utf8')
    connection.autocommit(True)
    # redundant sanitization because paranoia
    #arguments = sanitize_query(*args)
    try:
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.callproc(proc, args)
        row = cursor.fetchall()
        return make_response(jsonify({"status": "success", "result": row}), 200)
    except Exception, e:
        print e
    finally:
        cursor.close()
        connection.close()
    return make_response(jsonify({"status": "failure"}), 400)

# quickly validate and call the method passed to it
# sidenote, I wish there was a way to force validation using decorators
def validate():
    if 'username' in session:
        return True
    else:
        abort(403)
