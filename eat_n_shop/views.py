from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GrocerySerializer
from .models import Grocery

# Create your views here.
class GroceryView(viewsets.ModelViewSet):
    serializer_class = GrocerySerializer
    queryset = Grocery.objects.all()
