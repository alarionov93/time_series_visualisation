# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class TimeSeries(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название временного ряда')
    meta = models.CharField(max_length=255, verbose_name='описание, метаданные')

    @property
    def points(self):
        return Point.objects.filter(ts_id=self.id)

    def get_list_of_points(self):
        return [x.to_list() for x in self.points]

    class Meta:
        db_table = 'time_series'
        verbose_name = 'временной ряд'
        verbose_name_plural = 'временные ряды'

class Point(models.Model):
    ts_id = models.ForeignKey(to='TimeSeries', to_field='id', verbose_name='Id временного ряда')
    x_dim = models.FloatField(verbose_name='значение x')
    y_dim = models.FloatField(verbose_name='значение y')

    def to_json(self):
        return {
            'ts_id': self.ts_id,
            'x_dim': self.x_dim,
            'y_dim': self.y_dim
        }

    def to_list(self):
        return [
            self.x_dim,
            self.y_dim
        ]

    class Meta:
        db_table = 'points'
        verbose_name = 'точка'
        verbose_name_plural = 'точки'