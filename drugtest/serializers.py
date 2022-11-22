from rest_framework import serializers

from drugtest.models import DrugTestModel, QuestOrderModel
from company.serializers import UserCompanyModelSerializer

class QuestOrderModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestOrderModel
        fields = '__all__'
        #fields = ['first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'unique_id', 'is_active', 'id']


class DrugTestModelSerializer(serializers.ModelSerializer):
    order_details = QuestOrderModelSerializer()
    company = UserCompanyModelSerializer()
    class Meta:
        model = DrugTestModel
        fields = '__all__'
