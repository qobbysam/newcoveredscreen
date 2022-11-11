from rest_framework import serializers
from squarepayment.facade import Facade


class PaynowSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=200)


    def save_msg(self,user, validated_data):
        msg_out = {}
        token = validated_data['token']
        facade = Facade()

        res = facade.atomic_payment(token, user)

        return res
