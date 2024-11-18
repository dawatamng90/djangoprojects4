from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def display_time(request):
    time = datetime.datetime.now()
    msg = '<h1>Hello Friends. Good Evening!!!.</h1><hr>'
    msg += f'Now server time is {time}'
    return HttpResponse(msg)