#from django.db import models

from mongoengine import Document, StringField, IntField


# Create your models here.
class Article(Document):
	articleName = StringField(max_length=150)
	articleContent = StringField(max_length=200000)
	likes = IntField()
	dislikes = IntField()
	author = StringField(max_length=150)

	def _str_(self):
		return self._id