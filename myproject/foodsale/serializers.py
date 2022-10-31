from rest_framework import serializers
from .models import foodsale

class foodsaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodsale
        fields = ['OrderDate', 'Region', 'City', 'Category','Product','Quantity','UnitPrice']