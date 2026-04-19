from . import views
from django.urls import path

urlpatterns = [
    path("", views.ProductListCreateView.as_view(), name="product-list-create"),
    path("<int:pk>/", views.ProductRetrieveUpdateView.as_view(), name="product-retrieve-update"),
]