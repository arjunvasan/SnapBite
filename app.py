# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
app.config["COUCHDB_SERVER"] = "https://app4790148.heroku:snapbite@app4790148.heroku.cloudant.com"
app.config["COUCHDB_DATABASE"] = "restaurants"

from flaskext.couchdb import *


manager = CouchDBManager(auto_sync=False)
# ...add document types and view definitions...
manager.setup(app)
manager.sync(app)

@app.route('/')
def hello():
	document = dict(title="Jantas Restaurant", content="Hello, world!")
	manager.add_document(document)
	return 'Hello World!'

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)