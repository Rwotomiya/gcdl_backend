from rest_framework import serializers
from .models import Procurement, Stock, Produce

class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = '__all__'

class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
