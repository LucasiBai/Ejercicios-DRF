from rest_framework import viewsets

from cart.api.serializers import CartItemSerializer
from cart.models import CartItem


class CartItemApi(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
