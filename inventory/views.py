from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Procurement, Stock, Produce
from .serializers import ProcurementSerializer, StockSerializer, ProduceSerializer

class ProduceViewSet(viewsets.ModelViewSet):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer

class ProcurementViewSet(viewsets.ModelViewSet):
    queryset = Procurement.objects.all()
    serializer_class = ProcurementSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
