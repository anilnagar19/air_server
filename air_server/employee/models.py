from django.db import models


class Employee(models.Model):
    EMP_ID = models.CharField(max_length=200, unique=True)
    EMP_NAME = models.CharField(max_length=200, default='')
    EMP_MOBILE = models.CharField(max_length=10, default='')
    DEPARTMENT = models.CharField(max_length=200, default='')
    CREATED_AT = models.DateTimeField(auto_now_add=True)


class Temperature(models.Model):
    EMP_ID = models.CharField(max_length=200, default='', blank=True)
    TEMPERATURE = models.CharField(max_length=10)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
