from django.shortcuts import render
from ecomapp.models import Category, Product

def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'base.html', context)


def product_view(request, slug):
    product = Product.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
    }
    return render(request, 'product.html', context)


def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    products_of_category = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories,
    }
    return render(request, 'category.html', context) 