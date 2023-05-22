from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.


@api_view(["GET"])
def getAllEmployees(request):
    employees = Employee.objects.all()

    if request.method == "GET":
        serializer = EmployeeSerializer(employees, many=True)
        employees = serializer.data
        return Response(employees)


@api_view(["GET"])
def getEmployeeById(request, employeeId):
    employee = None

    try:
        employee = Employee.objects.get(employeeId=employeeId)
    except Employee.DoesNotExist as e:
        print("SUPRATIM:", e)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        employee = serializer.data
        return Response(employee)


@api_view(["POST"])
def addAnEmployee(request):
    if request.method == "POST":
        json = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=json)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print("SUPRATIM:", serializer.errors)
            return Response(serializer.errors)
