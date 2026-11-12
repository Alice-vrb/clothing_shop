from django.views import View
from django.http import HttpResponse, Http404
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ProductView(View):
    def dispatch(self, request, *args, **kwargs):
        print(request.method)
        print(request.path)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, product_id: int):
        if product_id > 100:
            raise Http404("Product not found")
        else:
            return HttpResponse(f"Product №{product_id}")

class CategoryView(View):
    def upper_case(self, text):
        return text.upper()

    def get(self, request, category_name: str):
        return HttpResponse(self.upper_case(category_name))

class SearchView(View):
    http_method_names = ['get', 'head']

    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            return HttpResponse(f"You searched: {query}")
        else:
            return HttpResponse("Enter a search query")
