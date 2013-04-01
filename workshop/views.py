# -*- coding: utf-8 -*- 

from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_list_or_404
import datetime
from models import ClientsPlaces

def homepage(request):
    now = datetime.datetime.now()
    t = get_template('homepage.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def show_map(request):
    clients = ClientsPlaces.objects.all()
    #clients = get_list_or_404 (ClientsPlaces, type = crimeType)
    return render_to_response ('map_yandex.html', locals())

