from django.shortcuts import render
from ecomapp.models import Category, Product, CartItem, Cart
from django.http import HttpResponseRedirect

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


def cart_view(request):
    categories = Category.objects.all()
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id=cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'cart': cart,
        'categories': categories,
    }

    return render(request, 'cart.html', context)


def add_to_cart_view(request, slug):
    product = Product.objects.get(slug=slug)
    new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
    cart = Cart.objects.first()
    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
        return HttpResponseRedirect('/cart/')