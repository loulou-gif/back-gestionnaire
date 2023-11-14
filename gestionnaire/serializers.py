from rest_framework import serializers
from .models import Stock, direction, UserDetail, Location, status_product, stock_category
from django.contrib.auth.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('direction', 'manager', 'numero')

class UserSerializer(serializers.ModelSerializer):
    userdetail = UserDetailSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'userdetail')

    def create(self, validated_data):
        userdetail_data = validated_data.pop('userdetail', None)
        user = User.objects.create(**validated_data)
        if userdetail_data:
            UserDetail.objects.create(user=user, **userdetail_data)
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
        fields= ('name', 'details')
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ("first_name","username","last_name","email","last_login","userdetails")