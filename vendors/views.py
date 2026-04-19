from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Vendor
from .serializers import VendorSerializer
from drf_yasg.utils import swagger_auto_schema


class VendorListCreateView(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @swagger_auto_schema(tags=["Vendors"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Vendors"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class VendorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @swagger_auto_schema(tags=["Vendors"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Vendors"])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Vendors"])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Vendors"])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)