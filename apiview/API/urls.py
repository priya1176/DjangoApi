from django.contrib import admin
from django.urls import path,include
from API.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employee',EmployeeViewSet)



urlpatterns = [
    path('',include(router.urls))

]

#companies/{companyId}/employees