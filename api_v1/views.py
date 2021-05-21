from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse(json.dumps({"token":"ok"}))
    return HttpResponseNotAllowed('Only GET request are allowed')


def api_add(request):
    if request.body:
        try:
            response_data = json.loads(request.body)
            add = int(response_data['A']) + int(response_data['B'])
            response_answer = {
                "answer": add
            }
            response = HttpResponse(json.dumps(response_answer))
            response['Content-Type'] = 'application/json'
            return response
        except:
            return for_exept()

def subtract_api(request):
    if request.body:
        try:
            response_data = json.loads(request.body)
            subtract = int(response_data['A']) - int(response_data['B'])
            response_answer = {
                "answer":  subtract
            }
            response = HttpResponse(json.dumps(response_answer))
            response['Content-Type'] = 'application/json'
            return response
        except:
            return for_exept()


def multiply_api(request):
    if request.body:
        try:
            response_data = json.loads(request.body)
            multiply = int(response_data['A']) * int(response_data['B'])
            response_answer = {
                "answer":  multiply
            }
            response = HttpResponse(json.dumps(response_answer))
            response['Content-Type'] = 'application/json'
            return response
        except:
            return for_exept()

def divide_api(request):
    if request.body:
        try:
            response_data = json.loads(request.body)
            divide = int(response_data['A']) / int(response_data['B'])
            response_answer = {
                "answer":  divide
            }
            response = HttpResponse(json.dumps(response_answer))
            response['Content-Type'] = 'application/json'
            return response
        except:
            return for_exept()

def for_exept():
    data = 'ERROR IN REQUEST XA XA XA'
    response_answer = {
        "answer": data
    }
    response = HttpResponse(json.dumps(response_answer))
    response['Content-Type'] = 'application/json'
    response.status_code = 400
    return response