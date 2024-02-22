from rest_framework import serializers
from .models import Article



class ArticleSerializer(serializers.Serializer):
  id = serializers.SerializerMethodField()
  articleName = serializers.CharField(max_length=150)
  articleContent = serializers.CharField(max_length=200000)
  likes = serializers.IntegerField()
  dislikes = serializers.IntegerField()
  author = serializers.CharField(max_length=150)

  def create(self, validated_data):
    return Article.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.articleName = validated_data.get('articleName', instance.articleName)
    instance.articleContent = validated_data.get('articleContent', instance.articleContent)
    instance.likes = validated_data.get('likes', instance.likes)
    instance.dislikes = validated_data.get('dislikes', instance.dislikes)
    instance.author = validated_data.get('author', instance.author)
    instance.save()
    return instance

  def get_id(self, obj):
    return str(obj.id)

  class Meta:
    model = Article
    fields = ('id', 'articleName', 'articleContent', 'likes', 'dislikes', 'author')


