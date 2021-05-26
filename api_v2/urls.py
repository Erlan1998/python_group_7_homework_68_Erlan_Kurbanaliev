from django.urls import path, include
from api_v2.views import ArticleView, Operation

app_name = 'api_v2'


article_urls = [
    path('', ArticleView.as_view(), name='articles'),
    path('<int:pk>/operation', Operation.as_view(), name='detail_articles'),

]

urlpatterns = [
    path('articles/', include(article_urls)),
]