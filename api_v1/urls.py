from django.urls import path

from api_v1.views import api_add, get_token_view, subtract_api, multiply_api, divide_api

app_name = 'api_v1'

urlpatterns = [
    path('add/', api_add, name='add_api'),
    path('subtract/', subtract_api, name='subtract_api'),
    path('multiply/', multiply_api, name='multiply_api'),
    path('divide/', divide_api, name='divide_api'),
    path('get_token/', get_token_view, name='get_token'),
]