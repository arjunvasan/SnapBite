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

'''
from struct import pack
from OpenSSL import SSL
from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory, Protocol
from twisted.internet.ssl import ClientContextFactory
import binascii
import struct

APNS_SERVER_HOSTNAME = "gateway.sandbox.push.apple.com"
APNS_SERVER_PORT = 2195
APNS_SSL_CERTIFICATE_FILE = "<your ssl certificate.pem>"
APNS_SSL_PRIVATE_KEY_FILE = "<your ssl private key.pem>"
DEVICE_TOKEN = "<hexlified device token>"
MESSAGE = '{"aps":{"alert":"twisted test"}}'


API_FORMAT = """

  # = [ORDER] Call URL =======================
  # ==========================================

  # http://snapbite.heroku.com/device_comm/order
	
  # = [ORDER] STANDARD PARAMETER FORMATS =====
  # ==========================================

  # restaurant_id     => 'SOME_RESTAURANT_ID'                                           (String)   
  # table             => '2'                                                            (String)   
  # dish              => 'Eggplant Parmesan'                                            (String)   
  # special           => 'Substitute marinara for the alfredo sauce on the pasta'       (String)

  # ==========================================
  # = DEFINE STANDARD RESPONSE OBJECT FORMAT =
  # ==========================================

  # status_code        => 200 (success) or 400 (failure)

	

"""

class APNSClientContextFactory(ClientContextFactory):
	def __init__(self):
		self.ctx = SSL.Context(SSL.SSLv3_METHOD)
		self.ctx.use_certificate_file(APNS_SSL_CERTIFICATE_FILE)
		self.ctx.use_privatekey_file(APNS_SSL_PRIVATE_KEY_FILE)

	def getContext(self):
		return self.ctx

class APNSProtocol(Protocol):

	def connectionMade(self):
		print "connection made"
		self.sendMessage(binascii.unhexlify(DEVICE_TOKEN), MESSAGE)
		self.transport.loseConnection()

	def sendMessage(self, deviceToken, payload):
		fmt = "!cH32sH%ds" % len(payload)
		command = '\x00'
		msg = struct.pack(fmt, command, 32, deviceToken,len(payload), payload)
		print "%s: %s" %(binascii.hexlify(deviceToken), binascii.hexlify(msg))
		self.transport.write(msg)

class APNSClientFactory(ClientFactory):
	def buildProtocol(self, addr):
		print "Connected to APNS Server %s:%u" % (addr.host, addr.port)
		return APNSProtocol()

	def clientConnectionLost(self, connector, reason):
		print "Lost connection. Reason: %s" % reason

	def clientConnectionFailed(self, connector, reason):
		print "Connection failed. Reason: %s" % reason
'''

@app.route('/device_comm/alert')
def alert():
	return "call waiter"

@app.route('/device_comm/order', methods=['POST','GET'])
def order():
	post = Order(
	    # Add id field if needed for vanity url
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
	
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        post = Restaurant(
            # Add id field if needed for vanity url
            name = request.form['name'],
            description = request.form['description'],
            location = request.form['location']
        )
        post.store()
        return 'You have signed up your restaurant!'
    else:
        return render_template('signup.html')

@app.route('/entermenudishes', methods=['POST', 'GET'])
def entermenudishes():
    if request.method== 'POST':
        post = Dishes(
            #Add id field
            restaurant = request.form['restaurant'],
            name = request.form['name'],
            price = request.form['price']
        )
        post.store()
        return 'You have added your menu dishes to our database.'
    else:
        return render_template('entermenudishes.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)