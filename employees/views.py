from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Employee
from employees.serializers import EmployeeSerializer
from accounts.permissions import IsAdminOrManager

# Create your views here.
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.select_related("user", "department")
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrManager]

class EmployeeDetailedAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.select_related("user", "department")
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrManager]