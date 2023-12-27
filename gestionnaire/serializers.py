from rest_framework import serializers
from .models import Stock, direction,  Location, status_product, stock_category
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    # userdetail = UserDetailSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name','is_staff', 'is_active', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Location
        fields = '__all__'
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stock
        fields = '__all__'
    
class directionSerializer(serializers.ModelSerializer):
    class Meta:
        model = direction
        fields= '__all__'
        
class status_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = status_product
        fields= '__all__'
        
class StockCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = stock_category
        fields= '__all__'
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ("first_name","username","last_name","email","last_login","userdetail",'id')