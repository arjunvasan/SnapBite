from flaskext.couchdb import *
class Restaurant(Document):
	doc_type = 'restaurant'
	name = TextField()
	description = TextField()
	tags = ListField(TextField())
	location = TextField()
	dishes = ListField(TextField())

class Order(Document):
	doc_type = 'order'
	restaurant = TextField()
	dish = TextField()
	special = TextField()
	table = IntegerField()
	placed = DateTimeField()

class Dishes(Document):
    doc_type = 'dishes'
    restaurant = TextField()
    name = TextField()
    price = FloatField()
    pictures = ListField(TextField())
    
    