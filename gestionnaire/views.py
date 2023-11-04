
from rest_framework import viewsets
from .models import Stock, direction
from django.contrib.auth.models import User
from .serializers import StockSerializer, UserSerializer, directionSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
        
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
class DirectionViewSet(viewsets.ModelViewSet):
    queryset = direction.objects.all()
    serializer_class = directionSerializer