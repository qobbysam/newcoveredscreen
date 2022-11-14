from rest_framework import serializers

from .models import UserCompanyModel

class UserCompanyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCompanyModel
        fields = '__all__'