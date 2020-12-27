
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name="home"),
    path('brands/', views.BrandListView.as_view(), name="brands"),
    path('brands/<int:pk>', views.BrandDetailView.as_view(), name="brand detail"),
]