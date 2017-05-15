# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Staff
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

def index(request):
    all_staff = Staff.objects.all()
    #information template needs
    context = {'all_staff': all_staff}
    return render(request, 'info/index.html', context)

def detail(request, staff_id):
    # staff = Staff.objects.get(pk=staff_id)
    staff = get_object_or_404(Staff, pk = staff_id)
    return render(request, 'info/detail.html', {'staff': staff})

def chosen(request):
    all_staff = Staff.objects.all()
    try:
        chosen_staff = all_staff.get(pk=request.POST['staff'])
    except (KeyError, chosen_staff.DoesNotExist):

        return render(request, 'info/index.html', {'staff': chosen_staff, 'error_message': "you did not chose a valid staff"})
    else:
        print("success")
        chosen_staff.is_chosen = True
        chosen_staff.save()
        return render(request, 'info/index.html')
