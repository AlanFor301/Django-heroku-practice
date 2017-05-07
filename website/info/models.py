# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=250)
    branch_location = models.CharField(max_length= 100)
    start_time = models.DateTimeField(default = '2016-01-01T10:20:05.123')
    end_time = models.DateTimeField(default = '2016-01-01T10:20:05.123')
    def __str__(self):
        return self.staff_name + ' - ' + self.branch_location + ' - ' + str(self.start_time) + ' to '+ str(self.end_time)
