from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/<int:product_id>/', views.product, name='products'),
    path('category/<slug:category_name>/', views.category, name='category'),
]