from rest_framework import generics, permissions, response, views
from . import serializers
from .models import Order


class CreateOrderView(generics.CreateAPIView):
    serializer_class= serializers.OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserOrderList(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        orders = user.orders.all()
        # orders = Order.objects.filter(user=user)
        serializer = serializers.OrderSerializer(orders, many=True).data
        return response.Response(serializer, status=200)


class UpdateOrderStatusView(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def patch(self, request, pk):
        status = request.data['status']
        if status not in ['in_process', 'closed']:
            return response.Response('Invalid Status', status=400)
        order = Order.objects.get(pk=pk)
        order.status = status
        order.save()
        serializer = serializers.OrderSerializer(order).data
        return response.Response(serializer, status=206)