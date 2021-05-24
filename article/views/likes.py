
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from article.models import ArticleLike, Article


class LikeforArticle(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            ArticleLike.objects.get(article=article, author=user)
            return HttpResponseForbidden('Вы уже поставили лайк)')
        except ArticleLike.DoesNotExist:
            ArticleLike.objects.create(article=article, author=user)
            return HttpResponse(article.Likes.count())

class UnlikeforArticle(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            unlike = ArticleLike.objects.get(article=article, author=user)
            unlike.delete()
            return HttpResponse(article.Likes.count())
        except ArticleLike.DoesNotExist:
            return HttpResponseForbidden('Вы еще не лайкнули)')