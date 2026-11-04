from django.urls import path
from .views import HomeView, AboutView, ProductView, CategoryView, SearchView
from django.views.generic import RedirectView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('product/<int:product_id>/', ProductView.as_view(), name='product'),
    path('category/<slug:category_name>/', CategoryView.as_view(), name='category'),
    path('search/', SearchView.as_view(), name='search'),
    path('old-home/', RedirectView.as_view(pattern_name='home', permanent=False), name='old-home'),
]