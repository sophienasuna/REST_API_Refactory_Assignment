from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Order
from .serializers import OrderSerializer
from drf_yasg.utils import swagger_auto_schema


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @swagger_auto_schema(tags=["Orders"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Orders"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @swagger_auto_schema(tags=["Orders"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Orders"])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Orders"])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Orders"])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)