from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Client
from .serializers import ClientSerializer
from drf_yasg.utils import swagger_auto_schema


class ClientListCreateView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @swagger_auto_schema(tags=["Clients"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clients"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ClientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @swagger_auto_schema(tags=["Clients"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clients"])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clients"])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clients"])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)