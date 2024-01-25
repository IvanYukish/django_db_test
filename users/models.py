# -*- coding: utf-8 -*-

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=63)


class Worker(models.Model):
    name = models.CharField(max_length=63)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    sector = models.CharField(max_length=63)
