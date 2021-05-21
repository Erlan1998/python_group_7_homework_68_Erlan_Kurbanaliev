from django.urls import path
from webapp.views import index


app_name = 'web'

urlpatterns = [
    path('', index, name='index'),
]