from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["employeeId", "firstName", "lastName"]

    def create(self, validated_data):
        print(f"SUPRATIM: Create method is ready to execute for {validated_data}")
        return Employee.objects.create(**validated_data)
