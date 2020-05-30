
from django.contrib import admin
from django.urls import path, include

from employee import views

urlpatterns = [
    path('', include('employee.urls'))
]
