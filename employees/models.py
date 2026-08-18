from django.db import models
from django.conf import settings

from accounts.models import User
from departments.models import Department


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )
    employee_code = models.CharField(max_length=20, unique=True)    
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="employees"
    )
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.employee_code}"
