#!/usr/bin/env python
import sys
from flask import Flask, jsonify, abort, request, make_response, session
from query_helper import *
from flask_restful import reqparse, Resource, Api
from flask_session import Session
from settings import *
import json
import ldap
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

####################################################################################
#
# Routing: GET and POST using Flask-Session
#
# Demonstration only!
#
class SignIn(Resource):
	#
	# Login, start a session and get session cookie
	#
	# Example curl command:
	# curl -i -H "Content-Type: application/json" -X POST -d '{"username": "Casper", "password": "c\*ap"}' -c cookie-jar http://info3103.cs.unb.ca:61340/signin
	#
	def post(self):

		if not request.json:
			abort(400) # bad request

		# Parse the json
		parser = reqparse.RequestParser()
 		try:
 			# Check for required attributes in json document, create a dictionary
	 		parser.add_argument('username', type=str, required=True)
			parser.add_argument('password', type=str, required=True)
			request_params = parser.parse_args()
		except:
			abort(400) # bad request

		if request_params['username'] in session:
			response = {'status': 'success'}
			responseCode = 200
		else:
			try:
				l = ldap.open(LDAP_HOST)
				l.start_tls_s()
				l.simple_bind_s("uid="+request_params['username']+
					", ou=People,ou=fcs,o=unb", request_params['password'])
				# At this point we have sucessfully authenticated.

				session['username'] = request_params['username']
				response = {'status': 'success', 'username': session['username'] }
				print "SESSION CREATED: " + session['username']
				responseCode = 201
			except ldap.LDAPError, error_message:
				response = {'status': 'Access denied', 'error': str(error_message)}
				responseCode = 403
			finally:
				l.unbind()

		return make_response(jsonify(response), responseCode)

	# GET: Check for a login
	#
	# Example curl command:
	# curl -i -H "Content-Type: application/json" -X GET -b cookie-jar
	#	http://info3103.cs.unb.ca:61340/signin
	def get(self):
		success = False
		if 'username' in session:
			response = {'status': 'success'}
			responseCode = 200
		else:
			response = {'status': 'fail'}
			responseCode = 403

		return make_response(jsonify(response), responseCode)

	# DELETE: Logout: remove session
	#
	# Example curl command:
	# curl -i -H "Content-Type: application/json" -X DELETE -b cookie-jar
	#	http://info3103.cs.unb.ca:61340/signin

	#
	#	Here's your chance to shine!
	#


####################################################################################
#
# Identify/create endpoints and endpoint objects
#
api = Api(app)
api.add_resource(SignIn, '/signin')


# xxxxx= last 5 digits of your studentid. If xxxxx > 65535, subtract 30000
if __name__ == "__main__":
    app.run(host = APP_HOST, port = APP_PORT, debug = APP_DEBUG)
