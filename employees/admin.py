from django.contrib import admin

from employees.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "employee_code",
        "department",
        "designation",
        "salary",
    )

    list_filter = (
        "department",
        "designation",
    )

    search_fields = (
        "employee_code",
        "email",
    )
