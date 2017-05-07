# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>this is your Info page</h1>")
def detail(request, staff_id):
    return HttpResponse("<h2>Details for staff id: "+ str(staff_id)+"</h2>")
