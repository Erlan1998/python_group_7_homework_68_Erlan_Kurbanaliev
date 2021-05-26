import json

from django.http import JsonResponse
from django.views import View

from article.models import Article
from api_v2.serializers import ArticleSerializer


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        response_data = ArticleSerializer(articles, many=True).data

        return JsonResponse(data=response_data, safe=False)

    def post(self, request, *args, **kwargs):
        article_data = json.loads(request.body)
        serializer = ArticleSerializer(data=article_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({})
        return JsonResponse({'error': 'Data not valid'}, status=404)