from rest_framework import serializers
from .models import Stock, direction
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username','email','password') 
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stock
        fields = '__all__'
    
class directionSerializer(serializers.ModelSerializer):
    class Meta:
        model = direction
        fields= '__all__'