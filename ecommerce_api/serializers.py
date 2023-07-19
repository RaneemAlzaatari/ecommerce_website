from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from ecommerce_api.models import Product ,ProductImg,Cart,CartItem

class SignupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
            validated_data["password"] = make_password(validated_data.get("password"))
            return super(SignupSerializer, self).create(validated_data)
    class Meta:
            model = User
            fields = ['username','email','password']

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
            model = User
            fields = ['username','password']

class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title','description','category','price','stock','condition','rating')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id','cartId','productId','quantity')

class CartItemAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields ='__all__'