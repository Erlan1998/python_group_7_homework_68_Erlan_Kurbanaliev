from django.urls import path

from api_v1.views import my_first_api_view
app_name = 'api_v1'

urlpatterns = [
    path('add/', my_first_api_view, name='add_api')
]