from django.shortcuts import render
from requests import request
from rest_framework import viewsets

class ShopViewSets(viewsets.ViewSet):
    def list(self,request):            #/api/shop  
        pass

    def create(self,request):          #/api/shop  
        pass
       
    def retrieve(self,request,pk=None): #/api/shop/<str:idx>
        pass
    
    def update(self,request,pk=None):   #/api/shop/<str:idx>
        pass
    def destroy(self,request,pk=None):  #/api/shop/<str:idx>
        pass

class OrderViewSets(viewsets.ViewSet):
    def list(self,request):            #/api/order  
        pass

    def create(self,request):          #/api/order  
        pass
       
    def retrieve(self,request,pk=None): #/api/order/<str:idx>
        pass
    
    def update(self,request,pk=None):   #/api/order/<str:idx>
        pass
    def destroy(self,request,pk=None):  #/api/order/<str:idx>
        pass