from rest_framework import serializers
from employee.models import Employee
from employee.models import Temperature


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'


class EmployeeTempSerializer(serializers.ModelSerializer):
    EMP_ID = serializers.CharField(source='EMP_ID.EMP_ID')
    EMP_MOBILE = serializers.CharField(source='EMP_ID.EMP_MOBILE')
    DEPARTMENT = serializers.CharField(source='EMP_ID.DEPARTMENT')
    EMP_NAME = serializers.CharField(source='EMP_ID.EMP_NAME')

    class Meta:
        model = Temperature
        fields = '__all__'
