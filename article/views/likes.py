
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from article.models import ArticleLike, Article, Comment, CommentLike


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


class LikeforComment(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            CommentLike.objects.get(comment=comment, author=user)
            return HttpResponseForbidden('Вы уже поставили лайк)')
        except CommentLike.DoesNotExist:
            CommentLike.objects.create(comment=comment, author=user)
            return HttpResponse(comment.Commentlikes.count())


class UnlikeforComment(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            unlike = CommentLike.objects.get(comment=comment, author=user)
            unlike.delete()
            return HttpResponse(comment.Commentlikes.count())
        except CommentLike.DoesNotExist:
            return HttpResponseForbidden('Вы еще не лайкнули)')
