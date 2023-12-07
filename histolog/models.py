from django.db import models

# Create your models here.

class Article(models.Model):
	articleName = models.CharField(max_length=150)
	articleContent = models.TextField()
	likes = models.IntegerField()
	dislikes = models.IntegerField()
	author = models.CharField(max_length=150)

	def _str_(self):
		return self._id