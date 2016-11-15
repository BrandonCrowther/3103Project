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
class StandardErrors(Resource):
    @app.route("/")
    def start():
        return "Wow this is the default directory!\n"

    @app.errorhandler(404)
    def not_found(error):
        return make_response("404 Not Found\n", 404)


# Comics
class Comics():
    @app.route("/comics/", methods=['GET', 'POST'])
    def comics():
        if request.method == 'GET':
            return build_response_auth("get_comics")
        elif request.method == 'POST':
            return build_response_auth("add_comic", scrape_json('comic'))

    @app.route("/comics/<int:comic_id>", methods=['GET', 'UPDATE', 'DELETE'])
    def get_comic(comic_id):
        if request.method == 'GET':
            return build_response_auth("get_comic", comic_id)
        elif request.method == 'UPDATE':
            return build_response_auth("update_comic", comic_id, request_params['comic'])
        elif request.method == 'DELETE':
            return build_response_auth("delete_comic", comic_id)

    # add this back later
    # @app.route("/comics/series/<int:series_id>")
    # def get_issues_from_series(series_id):
    #     return build_response("get_issues_from_series", series_id)
    #
    # @app.route("/comics/publisher/<int:publisher_id>")
    # def get_issues_from_publisher(publisher_id):
    #     return build_response("get_issues_from_publisher", publisher_id)
    #
    # @app.route("/comics/writer/<int:writer_id>")
    # def get_issues_from_writer(writer_id):
    #     return build_response("get_issues_from_writer", writer_id)


class SignIn(Resource):
	def post(self):
		if not request.json:
			abort(400)
		parser = reqparse.RequestParser()
 		try:
 			# Check for required attributes in json document, create a dictionary
	 		parser.add_argument('username', type=str, required=True)
			parser.add_argument('password', type=str, required=True)
			request_params = parser.parse_args()
		except:
			abort(400)
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

    # Unused, but available for curling
	def get(self):
		if 'username' in session:
			response = {'status': 'success'}
			responseCode = 200
		else:
			response = {'status': 'fail'}
			responseCode = 403
		return make_response(jsonify(response), responseCode)

        def delete(self):
            if 'username' in session:
                del session['username']
                response = {'status': 'success'}
                responseCode = 200
            else:
                response = {'status': 'fail'}
                responseCode = 403
            return make_response(jsonify(response), responseCode)



api = Api(app)
api.add_resource(SignIn, '/signin')

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(host = APP_HOST, port = APP_PORT, debug = APP_DEBUG)
