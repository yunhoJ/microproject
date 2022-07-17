from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import Order,Shop
from .serializers import ShopSerializers,OrderSerializers
class ShopViewSets(viewsets.ViewSet):
    def list(self,request):            #/api/shop  
        shops=Shop.objects.all() #shop의 내역을 가져오기
        serializer=ShopSerializers(shops,many=True)# json형태로 변환 
        return Response(serializer.data)

    def create(self,request):          #/api/shop  
        serializer=ShopSerializers(data= request.data)#포스트맨으로 보내진 json데이터
        serializer.is_valid(raise_exception=True)#해당 데이터가 유효한지 확인 유효하지 않으면 예외처리 해라  
        serializer.save()#데이터 저장 
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None): #/api/shop/<str:idx>
        shop=Shop.objects.get(id=pk)
        serializer=ShopSerializers(shop)
        return Response(serializer.data)
    
    def update(self,request,pk=None):   #/api/shop/<str:idx>
        shop=Shop.objects.get(id=pk)
        serializer=ShopSerializers(instance=shop,data=request.data)#해당 shop의 데이터를 request.data로 변경해라
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    def destroy(self,request,pk=None):  #/api/shop/<str:idx>
        shop=Shop.objects.get(id=pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
         
class OrderViewSets(viewsets.ViewSet):
    def list(self,request):            #/api/order  
        orders=Order.objects.all()
        serializer=OrderSerializers(orders,many=True)
        return Response(serializer.data)

    def create(self,request):          #/api/order  
        serializer=OrderSerializers(data= request.data)      
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None): #/api/order/<str:idx>
        order=Order.objects.get(id=pk)
        serializer=OrderSerializers(order)
        return Response(serializer.data)
    
    def update(self,request,pk=None):   #/api/order/<str:idx>
        order=Order.objects.get(id=pk)
        serializer=OrderSerializers(instance=order,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self,request,pk=None):  #/api/order/<str:idx>
        order=Order.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)