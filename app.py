# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration


app = Flask(__name__)
app.config["COUCHDB_SERVER"] = "https://app4790148.heroku:WgINDWRcjikDuH4K1bH7wFPg@app4790148.heroku.cloudant.com"
app.config["COUCHDB_DATABASE"] = "restaurants"

from flaskext.couchdb import *


manager = CouchDBManager()
# ...add document types and view definitions...
manager.setup(app)

@app.route('/')
def hello():
    document = dict(title="Jantas Restaurant", content="Hello, world!")
    g.couch["Janta's"] = document
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)