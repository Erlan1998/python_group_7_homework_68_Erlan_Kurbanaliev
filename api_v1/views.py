from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.


def my_first_api_view(request):
    response_data = {
     "A": 1234,
     "B": 4567
}
    response = HttpResponse(json.dumps(response_data))
    response['Content-Type'] = 'application/json'
    return response