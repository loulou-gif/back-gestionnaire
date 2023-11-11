
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Stock, direction, UserDetail, Location
from django.contrib.auth.models import User
from .serializers import StockSerializer, UserSerializer, directionSerializer, UserDetailSerializer, LocationSerializer

# Create your views here.
class UserViewSet(viewsets.ViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def list(self, request):
        user_details = UserDetail.objects.all()
        serializer = UserDetailSerializer(user_details, many=True)
        return Response(serializer.data)
        
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
class DirectionViewSet(viewsets.ModelViewSet):
    queryset = direction.objects.all()
    serializer_class = directionSerializer
    
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class= LocationSerializer