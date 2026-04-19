from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)
from .serializers import ProductSerializer, ProductCreateSerializer
from .models import Product
from drf_yasg.utils import swagger_auto_schema


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductSerializer  # cleaner than super()

    # ✅ Swagger tags belong here
    @swagger_auto_schema(tags=["Products"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Products"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class ProductRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(tags=["Products"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Products"])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)    