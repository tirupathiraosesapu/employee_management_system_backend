from django.urls import path

from employees.views import EmployeeDetailedAPIView, EmployeeListCreateAPIView
urlpatterns = [
    path("", EmployeeListCreateAPIView.as_view(), name="employee"),
    path("<int:pk>/", EmployeeDetailedAPIView.as_view(), name="detailed-employee-view")
]