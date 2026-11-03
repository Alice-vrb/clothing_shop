from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/<int:product_id>/', views.product, name='products'),
    path('category/<slug:category_name>/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('old-home/', RedirectView.as_view(pattern_name='home', permanent=False), name='old-home'),
]