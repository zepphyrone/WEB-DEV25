from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from .models import Category,Product

# Create your views here.
def listAllProductsHandler(request):
    products= Product.objects.all()
    products_json=[product.to_json() for product in products]

    return JsonResponse(products_json,safe=False)


def listOneProductHandler(request,pk=None):
    try:
        productById = Product.objects.get(id=pk)
        return JsonResponse(productById.to_json())
    except Category.DoesNotExist as e:
        return JsonResponse({
                'error':e
            })


def listAllCategoriesHandler(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_json = [category.to_json() for category in categories]
        return JsonResponse(categories_json, safe=False)
    


def listOneCategoryHandler(request,pk=None):
    try:
        category = Category.objects.get(id=pk)
        return JsonResponse(category.to_json())
    except Category.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })

def listProductsByCategoryIdHandler(request,pk=None):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category=category)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)