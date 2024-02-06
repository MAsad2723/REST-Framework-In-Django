from rest_framework import serializers
from api.models import Company
# Creating Serializers              #Converting models to json
# Creating Company Serializer
class CompanySeriaizer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__" #I want to include all the fields from Company