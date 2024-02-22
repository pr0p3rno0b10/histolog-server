#from django.contrib import admin
from .models import Article
from django_mongoengine import mongo_admin as admin


class ArticleAdmin(admin.DocumentAdmin):
	list_display = ('articleName', 'articleContent', 'likes', 'dislikes', 'author')

# Register your models here.

admin.site.register(Article, ArticleAdmin)