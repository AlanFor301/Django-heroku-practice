# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=250)
    branch_location = models.CharField(max_length= 100)
    available_time = models.DateTimeField()
