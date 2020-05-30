from employee.models import Employee, Temperature
from rest_framework import viewsets, permissions, generics, filters, mixins
from .serializers import EmployeeSerializer, EmployeeTempSerializer


class EmployeeViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Employee.objects.all()
        empid = self.request.query_params.get('EMP_ID', None)
        if empid is not None:
            queryset = queryset.filter(EMP_ID=empid)
        return queryset


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
