# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
app.config["COUCHDB_SERVER"] = "https://app4790148.heroku:WgINDWRcjikDuH4K1bH7wFPg@app4790148.heroku.cloudant.com"
app.config["COUCHDB_DATABASE"] = "restaurants"

from flaskext.couchdb import *


manager = CouchDBManager(auto_sync=False)
# ...add document types and view definitions...
manager.setup(app)
manager.sync(app)

@app.route('/device_comm/alert')
def alert():
	return "call waiter"

@app.route('/device_comm/order')
def order():
	order = {
		"dish":"Saag Paneer",
		"special":"Extra Spicy",
		"table":4
	}
	g.couch["order_1"] = order
	return "order food"

@app.route('/device_comm/checkout')
def checkout():
	# [orders], cc_info, table
	return "checkout"

@app.route('/create')
def create():
	document = dict(title="Jantas Restaurant", content="Hello, world!")
	g.couch["jantas"] = document
	return 'Hello World!'

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)