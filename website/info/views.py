# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Staff
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    all_staff = Staff.objects.all()
    #django will look for template folder
    template = loader.get_template('info/index.html')
    #information template needs
    context = {
        'all_staff': all_staff}
    return HttpResponse(template.render(context, request))

def detail(request, staff_id):
    return HttpResponse("<h2>Details for staff id: "+ str(staff_id)+"</h2>")
