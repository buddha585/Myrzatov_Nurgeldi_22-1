from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def main(request):
    if request.method == 'GET':
        return HttpResponse('SUCCESS!')

def hello(hi):
    return HttpResponse

def timed(datem):
    return HttpResponse(datetime)

def goodbye(bye):
    return HttpResponse