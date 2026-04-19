# core/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class HelloWorldView(APIView):
    def get(self, request):
        return Response(data={"message": "Hello, World!"}, status=200)
    
schema_view = get_schema_view(
    openapi.Info(
        title="Inventory & Order Management API",
        default_version='v1',
        description="API documentation for Inventory & Order Management system",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)    


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("accounts/", include("django.contrib.auth.urls")), 
    path("", HelloWorldView.as_view(), name="hello_world"),
    path("api/v1/products/", include("products.urls")),
    path("api/v1/vendors/", include("vendors.urls")),
    path("api/v1/clients/", include("clients.urls")),
    path("api/v1/orders/", include("orders.urls")),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name='schema-redoc'),
]