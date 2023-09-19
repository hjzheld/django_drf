from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def articleAPI(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)    
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def articleDetailAPI(request, article_id):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)    
        return Response(serializer.data)
    elif request.method == "PUT":
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_200_OK)