from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySeriaizer, EmployeeSeriaizer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySeriaizer
    # Custom API : companies/{company_id}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=True):
        try:
            company = Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer = EmployeeSeriaizer(emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e: 
            print(e)
            return Response({'message':'No Employees :( )'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSeriaizer