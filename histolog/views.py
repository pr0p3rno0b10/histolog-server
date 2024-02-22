from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView


class ArticleDetailView(APIView):

  def get_object(self, id):
    try:
      article = Article.objects.get(id=id)
      article.reload()
      return article
    except Article.DoesNotExist:
      return None

  def get(self, request, id, format=None):
    article = self.get_object(id)
    article.reload()
    if article is not None:
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
    else:
      return Response(status=status.HTTP_404_NOT_FOUND)


  def put(self, request, id):
    try:
      article = Article.objects.get(id=id)
      article.reload()
    except Article.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ArticleListView(ListAPIView):
  serializer_class = ArticleSerializer

  def get_queryset(self):
    # Fetch all article IDs
    article_ids = Article.objects.all().scalar('id')
    # Re-fetch each article individually to ensure freshness (not recommended for performance reasons)
    articles = [Article.objects.get(id=article_id) for article_id in article_ids]
    return articles