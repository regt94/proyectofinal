from django.shortcuts import render
from .models import Order, OrderDetail
from carrito.models import ShoppingCart
from .serializers import OrderDetailSerializer,OrderSerializer
from rest_framework import viewsets
from rest_framework import permissions
from json import loads
from .paypal import GetOrder
from .utils import random_code
from django.http.response import JsonResponse
# from rest_framework import generics
# from rest_framework import filters

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (permissions.IsAuthenticated, )

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


  
# class PaymentCheckout(APIView):
#     def post(self, request):
#         data_unicode = request.data.decode('utf-8')
#         data = loads(data_unicode)
#         order_id = data['orderID']
#         # shopping_cart = ShoppingCart.objects.filter(user=request.user).all()
#         # total_price = round(sum(round((d.price), 2) for d in shopping_cart), 2)
#         order = GetOrder().get_order(order_id)
#         # order_price = float(order.result.purchase_units[0].amount.value)
#         # if order_price == total_price:
#         order_capture = GetOrder().capture_order(order_id, debug=True)
#         if order_capture:
#           code = f'PA-{random_code(5)}'
#           # order = Order.objects.create(price=order_price, user=request.user, code=code)
#           # if order:
#           #     order_id = order.pk
#           #     for value in shopping_cart:
#           #         OrderDetail.objects.create(order_id=order_id, product_id=value.product.id, price=value.price)
#           #     ShoppingCart.objects.filter(user=request.user).delete()

#           data = {
#               "id": order_capture.result.id,
#               "name": order_capture.result.payer.name.given_name
#           }

#           return JsonResponse(data)

#         return JsonResponse({
#             'error': 'No ocurrio nada'
#         })

