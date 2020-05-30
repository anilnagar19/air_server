from rest_framework import serializers
from employee.models import Employee
from employee.models import Temperature


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeTempSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperature
        fields = '__all__'
