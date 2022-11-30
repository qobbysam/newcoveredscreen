from rest_framework import serializers
from oscar.core.loading import (
    get_class, get_classes, get_model, get_profile_class)

UserAddress = get_model('address', 'UserAddress')

class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields= '__all__'