from mongoengine import *

class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=50)

class IA(Document):
    user = ReferenceField(User)
    code = StringField(max_length=50)
    points = StringField(max_length=50)