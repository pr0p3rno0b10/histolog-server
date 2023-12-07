from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('articleName', 'articleContent', 'likes', 'dislikes', 'author')

# Register your models here.

admin.site.register(Article, ArticleAdmin)