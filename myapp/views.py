from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from myapp.models import Employee
from myapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
