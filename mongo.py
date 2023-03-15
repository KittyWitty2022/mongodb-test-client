from mongoengine import *
from pymongo import MongoClient

client = MongoClient("mongodb+srv://artkittywitty:Yh9nW31GlmTHWPmz@kittywittydb.0d0dir0.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('cats')
records = db.cat_breed #MongoDB cloud shows CatBreed object under collection 'cat_breed' despite never making 'cat_breed' in specific
counted = records.count_documents({}) #If records were seen through 'CatBreed', counted documents will result in 0
print("Hi I'm here, there are this many records:", counted)

#NTS:put the uri like what's for client into the host parameter of connect for cloud db
connect(db="cats", host="mongodb+srv://artkittywitty:Yh9nW31GlmTHWPmz@kittywittydb.0d0dir0.mongodb.net/?retryWrites=true&w=majority")

#Creating object (class) with specified fields (constructs and paremeters)
class CatBreed(Document):
    breed = StringField(required=True, max_length=64)
    style = StringField(max_length=255)
    number_of_subspecies = IntField()

#Creating a record with created object above
b = CatBreed (
    breed = "Maine Coon",
    style="Gentle",
    number_of_subspecies = 3
)

b.save()
