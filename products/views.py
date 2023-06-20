from django.shortcuts import render
# Create your views here.
from products.models import Product, ProductCategory
def index(request):
    context = {'Title': 'Home',
               'is_promotion': True,
    }
    return render(request,'products/index.html', context)
def products(request):
    context ={
    'Title': 'Каталог',
    'products': Product.objects.all(),
    'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
