from flaskext.couchdb import *
class Restaurant(Document):
	doc_type = 'restaurant'
	person = TextField()
	description = TextField()
	tags = ListField(TextField())
	location = TextField()

class Order(Document):
	doc_type = 'order'
	restaurant = TextField()
	dish = TextField()
	special = TextField()
	table = IntegerField()
	placed = DateTimeField()
	