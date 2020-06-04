from employee.models import Employee, Temperature
from rest_framework import viewsets, permissions, generics, filters, mixins
from .serializers import EmployeeSerializer, EmployeeTempSerializer, TempSerializer

from django.http import JsonResponse
from rest_framework.response import Response
import json


class EmployeeViewSet(viewsets.ModelViewSet, mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = EmployeeSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Employee.objects.all()
        empid = self.request.query_params.get('EMP_ID', None)
        if empid is not None:
            queryset = queryset.filter(EMP_ID=empid)
        return queryset


class TemperatureViewSet(viewsets.ModelViewSet, mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = TempSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Temperature.objects.all()
        empid = self.request.query_params.get('EMP_ID', None)

        if empid is not None:
            Emp_id = Employee.objects.get(EMP_ID=empid)
            queryset = queryset.filter(EMP_ID=Emp_id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = TempSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class EmployeeTempViewSet(viewsets.ModelViewSet, mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = EmployeeTempSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Temperature.objects.all()
        empid = self.request.query_params.get('EMP_ID', None)

        if empid is not None:
            queryset = queryset.filter(EMP_ID=empid)
        return queryset
