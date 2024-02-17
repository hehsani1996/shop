from django.urls import path,include
from .views import ProductsListView, ProductsDetailView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('<int:pk>/',ProductsDetailView.as_view(), name='product_detail'),
]
