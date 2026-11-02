from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
    return HttpResponse("Clothes shop")

def about(request):
    return HttpResponse("This is a clothes shop.")

def product(request, product_id: int):
    if product_id > 100:
        return HttpResponseNotFound("Product not found")
    else:
        return HttpResponse(f"Product №<{product_id}>")

def category(request, category_name: str):
    return HttpResponse(category_name.upper())

def search(request):
    query = request.GET.get('q', '')
    if query:
        return HttpResponse(f"You searched: {query}")
    else:
        return HttpResponse("Enter a search query")
