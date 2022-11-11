from rest_framework import serializers

from shop import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["name", "code"]