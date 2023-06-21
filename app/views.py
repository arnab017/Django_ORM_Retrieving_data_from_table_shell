from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def input_topic(request):
    t = input('Enter topic name : ')
    TO = Topic.objects.get_or_create(topic_name=t)[0]
    TO.save()
    return HttpResponse('topic created')

def input_webpage(request):
    t = input('Enter topic name : ')
    TO = Topic.objects.get_or_create(topic_name=t)[0]
    TO.save()
    n = input('Enter web page name : ')
    u = input('Enter url : ')
    WO = Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('webpage created')

def input_ar(request):
    t = input('Enter topic name : ')
    TO = Topic.objects.get_or_create(topic_name=t)[0]
    TO.save()
    n = input('Enter web page name : ')
    u = input('Enter url : ')
    WO = Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d = input('Enter date(yyyy-mm-dd) : ')
    a = input('Enter author name : ')
    ARO = AccessRecords.objects.get_or_create(name=WO,date=d,author=a)[0]
    ARO.save()
    return HttpResponse('access record created')
