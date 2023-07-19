from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from .serializers import LoginSerializer ,ProductSerializer,ProductPostSerializer,ProductImageSerializer,CartSerializer,CartItemSerializer,CartItemAllSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from ecommerce_api.models import Product,CartItem,ProductImg
from rest_framework import generics,filters

class SignupAPIView(APIView):

    def post(self,request):
            serializer = SignupSerializer(data = request.data)
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                    username = serializer.validated_data["username"]
                    password = serializer.validated_data["password"]
                    user = authenticate(request, username=username, password=password)
                    print("user",user)
                    if user is not None:
                        token = Token.objects.get(user=user)
                        response = {
                               "status": status.HTTP_200_OK,
                               "message": "success",
                               "data": {
                                       "Token" : token.key
                                       }
                               }
                        return Response(response, status = status.HTTP_200_OK)
                    else :
                        response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Email or Password",
                               }
                        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
            response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": serializer.errors
                 }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)

class CreateProduct(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request, format=None):
        serializer = ProductPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllProducts(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class DetailsProduct(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request, pk, format=None):

        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
class DetailsProduct(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request, pk, format=None):

        try:
           product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
              return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
class UpdateProduct(APIView):
    permission_classes = [ IsAuthenticated ]

    def put(self, request, pk, format=None):
        try:
            res = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductPostSerializer(res, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteProduct(APIView):
    permission_classes = [ IsAuthenticated ]

    def delete(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

      
        product.delete() 
        return Response({'message': 'product was deleted successfully!'},status=status.HTTP_200_OK)

class AddImageProduct(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request, format=None):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageProductById(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request,pk, format=None):
     
        try:
            productImg = ProductImg.objects.get(productId=pk)
        except ProductImg.DoesNotExist:
              return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductImageSerializer(productImg)
        return Response(serializer.data)

class CreateCart(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddProductToCart(APIView):
    permission_classes = [ IsAuthenticated ]
    def post(self, request, format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            cart=CartItem.objects.filter(productId=request.data['productId'],cartId=request.data['cartId'])
            if cart:
                cart=cart.first()
                cart.quantity+=int(request.data['quantity'])
                cart.save()
                new_serializer = CartItemSerializer(cart)
                return Response(new_serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartItemById(APIView):
    permission_classes = [ IsAuthenticated ]

    def get(self, request, pk, format=None):
        try:
           cartitem = CartItem.objects.get(id=pk)
        except CartItem.DoesNotExist:
              return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CartItemAllSerializer(cartitem)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            cartitem = CartItem.objects.get(id=pk)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CartItemSerializer(cartitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CheckoutProduct(APIView):
    permission_classes = [ IsAuthenticated ]

    def delete(self, request, pk, format=None):
        try:
            cartitem = CartItem.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cartitem.delete() 
        return Response({'message': 'checkout product successfully!'},status=status.HTTP_200_OK)

class PartCheckoutProduct(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request, format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            cart=CartItem.objects.filter(productId=request.data['productId'],cartId=request.data['cartId'])
            if cart:
                cart=cart.first()
                if cart.quantity - int(request.data['quantity']) <= 0:
                    cart.delete() 
                    return Response({'message': 'checkout product successfully!'},status=status.HTTP_200_OK)
                else:
                    cart.quantity -= int(request.data['quantity'])
                    cart.save()
                    new_serializer = CartItemSerializer(cart)
                    return Response(new_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchProduct(generics.ListAPIView):
    permission_classes = [ IsAuthenticated ]

    search_fields = ('title','description','category')
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    