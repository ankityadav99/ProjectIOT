from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductInfo, ProductionProductInfo, ProductFeedback
from .serializer import ProductInfoSerializer, \
    ProductionProductInfoSerializer, \
    ProductFeedbackSerializer


# Create your views here.
class ProductInfoView(viewsets.ModelViewSet):
    """
    ModelViewSet is going to takecare lot of stuff for us
    1) Perform all operation of HTTP (POST/PUT/GET)
    2) Dont have explicitilty mention these methods
    3) Mostly these methods are common and every one is doing the same, better to use inbuilt
    4) Also instead of handling every case explicitly we are using the ModelViewSet
    """
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer


class ProductionProductInfoView(viewsets.ModelViewSet):
    queryset = ProductionProductInfo.objects.all()
    serializer_class = ProductionProductInfoSerializer


class ProductFeedbackView(viewsets.ModelViewSet):
    queryset = ProductFeedback.objects.all()
    serializer_class = ProductFeedbackSerializer

