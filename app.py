# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
app.config["COUCHDB_SERVER"] = "https://app4790148.heroku:WgINDWRcjikDuH4K1bH7wFPg@app4790148.heroku.cloudant.com"
app.config["COUCHDB_DATABASE"] = "snapbite"

from flaskext.couchdb import *

from models import *


manager = CouchDBManager(auto_sync=False)
# ...add document types and view definitions...
manager.setup(app)
manager.sync(app)

@app.route('/device_comm/alert')
def alert():
	return "call waiter"

@app.route('/device_comm/order', methods=['POST','GET'])
def order():
	post = Order(
		dish=request.args.get("dish"), 
		special=request.args.get("special"), 
		table=int(request.args.get("table"))
	)
	
	post.store()
	
	
	return "order food"
	

	
@app.route('/device_comm/checkout')
def checkout():
	# [orders], cc_info, table
	return "checkout"


blah = """
@app.route('/create')
def create():
	document = {
		"doc":"wef"
	}
	g.couch["jantas"] = document
	return 'Hello World!'
"""

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)