# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=250)
    branch_location = models.CharField(max_length= 100)
    start_time = models.DateTimeField(default = datetime.today())
    end_time = models.DateTimeField(default = datetime.today())
    is_chosen = models.BooleanField(default = False)
    def __str__(self):
        return self.staff_name + ' - ' + self.branch_location + ' - ' + str(self.start_time) + ' to '+ str(self.end_time)
