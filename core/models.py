# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class TimeSeries(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название временного ряда')

# Create your models here.
