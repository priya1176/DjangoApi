from django.shortcuts import render
from rest_framework import viewsets
from API.models import Company,Employee
from API.Serializers import Companyserializers, Employeeserializers

from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=Companyserializers  

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):

        company=company.objects.get(pk=pk)
        emps=Employee.objects.filter(company=company)
        emps_Serializer=Employeeserializers(emps,many=True,context={'request':request})
        return Response(emps_Serializer.data)
        

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Companyserializers
