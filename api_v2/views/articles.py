from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from api_v2.serializers import ArticleSerializer, article


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        response_data = ArticleSerializer(articles, many=True).data

        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        article_data = request.data
        serializer = ArticleSerializer(data=article_data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response({'id': article.pk})


class Operation(APIView):
    def get(self, request, pk, *args, **kwargs):
        context = {}
        article = Article.objects.filter(pk=pk)
        serializer = ArticleSerializer(article, many=True).data
        context['data_article'] = serializer
        return Response(context, status=200)

    def put(self, request, pk, *args, **kwargs):
        article_upd = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article_upd, data=request.data)
        serializer.is_valid(raise_exception=True)
        article_s = serializer.save()
        return Response({'id': article_s.pk})

    def delete(self, request, pk, *args, **kwargs):
        article_del = get_object_or_404(Article, pk=pk)
        print(article_del)
        article_del.delete()
        return Response(status=200)