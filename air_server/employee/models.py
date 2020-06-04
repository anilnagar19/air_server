from django.db import models


class Employee(models.Model):
    EMP_ID = models.CharField(max_length=200, primary_key=True)
    EMP_NAME = models.CharField(max_length=200, default='')
    EMP_MOBILE = models.CharField(max_length=10, default='')
    DEPARTMENT = models.CharField(max_length=200, default='')
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.EMP_ID


class Temperature(models.Model):
    EMP_ID = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='Temperature',)
    TEMPERATURE = models.CharField(max_length=10)
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '__all__'
