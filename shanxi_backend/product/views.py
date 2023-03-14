from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


@require_http_methods(["POST"])
def get_product(request):
    if request.method == "POST":
        try:
            get_name = request.POST.get('name')
            if get_name == '':
                products = Product.objects.all()
                return_products = serializers.serialize('json', products, ensure_ascii=False)
                return HttpResponse(return_products)

            products = Product.objects.filter(name__contains=get_name)

            if len(products) == 0:
                return HttpResponse("Haven't found")
            return_products = serializers.serialize('json', products, ensure_ascii=False)
            return HttpResponse(return_products)

        except BaseException:
            return HttpResponse("error")


@require_http_methods(["POST"])
def get_collections(request):
    if request.method == "POST":
        try:
            collections = Product.objects.filter(isCollection=True)
            return_collections = serializers.serialize('json', collections, ensure_ascii=False)
            return HttpResponse(return_collections)

        except BaseException:
            return HttpResponse("error")


@require_http_methods(["POST"])
def collect(request):
    if request.method == "POST":
        try:
            get_name = request.POST.get("name")
            product = Product.objects.get(name=get_name)
            product.isCollection = True
            product.save()
            return HttpResponse("succeed")

        except BaseException:
            return HttpResponse("error")


@require_http_methods(["POST"])
def delete_collection(request):
    if request.method == "POST":
        try:
            get_name = request.POST.get("name")
            product = Product.objects.get(name=get_name)
            product.isCollection = False
            product.save()
            return HttpResponse("succeed")

        except BaseException:
            return HttpResponse("error")