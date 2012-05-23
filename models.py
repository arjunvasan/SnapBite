from flaskext.couchdb import Document
class Restaurant(Document):
	doc_type = 'restaurant'
	name = TextField()
	description = TextField()
	tags = ListField(TextField())
	location = TextField()

class Order(Document):
	doc_type = 'order'
	restaurant = TextField()
	dish = TextField()
	special = TextField()
	table = IntegerField()
	