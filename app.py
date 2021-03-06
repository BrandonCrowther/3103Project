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
class Root(Resource):
    @app.route("/")
    def start():
        return app.send_static_file('index.html')

    @app.route("/validate_login")
    def login():
        if 'username' in session:
            return app.send_static_file('query_builder.html')
        else:
            return app.send_static_file('login.html')

    @app.route('/view_add_comic_book')
    def render_add_comic():
        return app.send_static_file('add_comic_book.html')

    @app.route('/view_add_publisher')
    def view_add_comic_book():
        return app.send_static_file('add_publisher.html')

    @app.route('/view_add_series')
    def view_add_series():
        return app.send_static_file('add_series.html')

    @app.route('/view_add_writer')
    def view_add_writer():
        return app.send_static_file('add_writer.html')

    @app.route('/view_edit_comic')
    def edit_comic():
        return app.send_static_file('update_comic_book.html')


# Comics
class Comics(Resource):
    def get(self):
        return build_response_auth("get_comics", session['username'])
    def post(self):
        return build_response_auth("add_new_issue", *scrape_json('comic', comics=True))
class ComicsResource(Resource):
    def get(self, comic_id):
        return build_response_auth("get_issue", comic_id)
    def put(self, comic_id):
        return build_response_auth("update_issue", comic_id, *scrape_json('comic'))
    def delete(self, comic_id):
        return build_response_auth("delete_issue", comic_id)

    @app.route("/comic/series/<int:series_id>")
    def get_issues_from_series(series_id):
        return build_response_auth("get_comics_by_series", session['username'], series_id)

    @app.route("/comic/publisher/<int:publisher_id>")
    def get_issues_from_publisher(publisher_id):
        return build_response_auth("get_comics_by_publisher", session['username'], publisher_id)

    @app.route("/comic/writer/<int:writer_id>")
    def get_issues_from_writer(writer_id):
        return build_response_auth("get_comics_by_writer", session['username'], writer_id)


# Deletes for everything but comics have been removed
# as a result of the database design
class Writers(Resource):
    def get(self):
        return build_response_auth("get_writers")
    def post(self):
        return build_response_auth("add_new_writer", *scrape_json('writer'))
class WritersResource(Resource):
    def get(self, writer_id):
        return build_response_auth("get_writer", writer_id)
    def put(self, writer_id):
        return build_response_auth("update_writer", writer_id, *scrape_json('writer'))
    # def delete(self, writer_id):
    #     return build_response_auth("delete_writer", writer_id)

class Publishers(Resource):
    def get(self):
        return build_response_auth("get_publishers")
    def post(self):
        return build_response_auth("add_new_publisher", *scrape_json('publisher'))
class PublishersResource(Resource):
    def get(self, publisher_id):
        return build_response_auth("get_publisher", publisher_id)
    def put(self, publisher_id):
        return build_response_auth("update_publisher", publisher_id, *scrape_json('publisher'))
    # def delete(self, publisher_id):
    #     return build_response_auth("delete_publisher", publisher_id)

class Series(Resource):
    def get(self):
        return build_response_auth("get_series")
    def post(self):
        return build_response_auth("add_new_series", *scrape_json('series'))
class SeriesResource(Resource):
    def get(self, series_id):
        return build_response_auth("get_specific_series", series_id)
    def put(self, series_id):
        return build_response_auth("update_series", series_id, *scrape_json('series'))
    # def delete(self, series_id):
    #     return build_response_auth("delete_series", series_id)

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
    		session['username'] = request_params['username']
    	else:
    		try:
    			l = ldap.open(LDAP_HOST)
    			l.start_tls_s()
    			l.simple_bind_s("uid="+request_params['username']+
    				", ou=People,ou=fcs,o=unb", request_params['password'])
    			# At this point we have sucessfully authenticated.

    			session['username'] = request_params['username']
    			response = {'status': 'success', 'username': session['username'] }
    			print("SESSION CREATED: " + session['username'])
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
api.add_resource(SignIn,                '/signin', '/login')
api.add_resource(Comics,                '/comic', '/comic/', '/comics', '/comics/')
api.add_resource(ComicsResource,        '/comic/<comic_id>', '/comics/<comic_id>')
api.add_resource(Publishers,            '/publisher', '/publisher/', '/publishers', '/publishers/')
api.add_resource(PublishersResource,    '/publisher/<publisher_id>', '/publishers/<publisher_id>')
api.add_resource(Writers,               '/writer', '/writer/', '/writers', '/writers/')
api.add_resource(WritersResource,       '/writer/<writer_id>', '/writers/<writer_id>')
api.add_resource(Series,                '/series', '/series/')
api.add_resource(SeriesResource,        '/series/<series_id>')

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(host = APP_HOST, port = APP_PORT, debug = APP_DEBUG, ssl_context=context)
