
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Stock, direction, UserDetail, Location, status_product, stock_category
from django.contrib.auth.models import User
from .serializers import StockSerializer, UserSerializer, directionSerializer, LocationSerializer, status_productSerializer, StockCategorieSerializer, UserListSerializer

# Create your views here.
class UserViewSet(viewsets.ViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    # def create(self, request, *args, **kwargs):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
class DirectionViewSet(viewsets.ModelViewSet):
    queryset = direction.objects.all()
    serializer_class = directionSerializer
    
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class= LocationSerializer
    
class statusProductViewSet(viewsets.ModelViewSet):
    queryset = status_product.objects.all()
    serializer_class = status_productSerializer
    
class categorieStockViewSet(viewsets.ModelViewSet):
    queryset = stock_category.objects.all()
    serializer_class = StockCategorieSerializer
    
class UserListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer