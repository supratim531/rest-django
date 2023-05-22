from django.urls import path
from .views import *


urlpatterns = [
    path('add', addAnEmployee, name="addAnEmployee"),
    path('fetch-all', getAllEmployees, name="getAllEmployees"),
    path('fetch/<employeeId>', getEmployeeById, name="getEmployeeById")
]
