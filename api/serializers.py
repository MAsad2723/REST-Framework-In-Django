from rest_framework import serializers
from api.models import Company, Employee
# Creating Serializers              #Converting models to json
# Creating Company Serializer
class CompanySeriaizer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__" #I want to include all the fields from Company
class EmployeeSeriaizer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__" #I want to include all the fields from Company