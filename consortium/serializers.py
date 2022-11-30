from rest_framework import serializers

from consortium.models import ConsortiumModel

class ConsortiumModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsortiumModel
        fields = '__all__'