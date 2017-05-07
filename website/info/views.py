# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Staff
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    all_staff = Staff.objects.all()
    #information template needs
    context = {'all_staff': all_staff}
    return render(request, 'info/index.html', context)

def detail(request, staff_id):
    try:
        staff = Staff.objects.get(pk=staff_id)
    except Staff.DoesNotExist:
        raise Http404("staff does not exist!")

    return render(request, 'info/detail.html', {'staff': staff})
