#coding=utf-8
from mongoengine.document import Document
from mongoengine.fields import StringField, BooleanField, ReferenceField

class IA(Document):
    name = StringField()
    code = StringField()
    isValidated = BooleanField()


class User(Document):
    ia = ReferenceField(IA)
    mail = StringField()
    name = StringField()
    password = StringField()

