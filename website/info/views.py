# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Staff
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #connect to the database. And get all data in Staff
    all_staff = Staff.objects.all()
    html = ''
    for staff in all_staff:
        url = '/info/' + str(staff.id) +"/"
        html += '<a href = "'+ url +'">' + staff.staff_name + '</a><br>'

    return HttpResponse(html)
def detail(request, staff_id):
    return HttpResponse("<h2>Details for staff id: "+ str(staff_id)+"</h2>")
