from django.db import models


# Create your models here.


class Employee(models.Model):
    employeeId = models.IntegerField()
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.employeeId}-{self.firstName}-{self.lastName}"
