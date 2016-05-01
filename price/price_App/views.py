from django.shortcuts import render
from price_App.models import ProductPrice, Price, Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date, timedelta
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

@api_view(['GET','POST'])
def product_price(request, pk):
    r = redis.Redis(connection_pool=pool)
    if request.method == 'POST':
        try:
            data = request.data
            price = data.pop('price')
            pri = Price(price = price)
            pri.save()
            product = Product.objects.get(id = pk)
            pro_pri = ProductPrice(price = pri, product = product)
            pro_pri.save()
            return Response({"status":"success", "message":"Product Price created"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"status":"fail", 'message':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET': 
        try:
            response = {}
            redis_key = str(pk) + '|' + str(date.today())
            value = r.get(redis_key)
            if value != None:
               price = value
            else: 
               pro_pri = ProductPrice.objects.get(product = pk, date = date.today())
               price = Price.objects.get(id = pro_pri.price_id).price  
               r.set(redis_key, price)
            product_name = Product.objects.get(id = pk)
            response['name'] = product_name.name
            response['price'] = str(price)
            response['product_id'] = pk
            return Response(response)
        except Exception as ex:
            return Response({'status': 'fail', 'message': str(ex)}) 

@api_view(['GET'])
def product_history(request, pk):
    r = redis.Redis(connection_pool=pool)
    if request.method == 'GET':
       try:
          response = {}
          redis_key = str(pk) + '|' + str(date.today()) + 'his'
          value = r.lrange('redis_key', 0, -1)
          if value != []:
             price = value
          else:
             price_ids = ProductPrice.objects.filter(product = Product.objects.get(id = pk), date__range = [date.today() - timedelta(30), date.today()]).values_list('price',flat=True)
             prices = Price.objects.filter(id__in = price_ids).order_by('id').values_list('price', flat = True)
             r.rpush(redis_key, *prices)
          response['prices'] = prices
          return Response(response)
       except Exception as ex:
          return Response({'status':'fail', 'message':str(ex)})
