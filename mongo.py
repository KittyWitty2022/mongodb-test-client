from mongoengine import *
from pymongo import MongoClient

client = MongoClient("mongodb+srv://artkittywitty:Yh9nW31GlmTHWPmz@kittywittydb.0d0dir0.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('cats')
records = db.CatBreeds
records.count_documents({})
print("Hi I'm here")
# #connect(db="cats", host="localhost")
# class CatBreed(Document):
#     breed = StringField(required=True, max_length=64)
#     style = StringField(max_length=255)
#     number_of_subspecies = IntField()

# b = CatBreed (
#     breed = "Siamese",
#     style="Fancy",
#     number_of_subspecies = 5
# )

# b.save()
