from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    user_email = serializers.CharField(source="user.email", read_only=True)
    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = Employee
        fields = (
            "id",
            "user",
            "username",
            "user_email",
            "employee_code",
            "department",
            "department_name",
            "designation",
            "salary",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
