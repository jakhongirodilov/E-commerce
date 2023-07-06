from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Category
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from . forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/index.html', context)


def display_category(request):
    if request.method == 'POST':
        if request.POST['category'] == 'all':
            products = Product.objects.all()
            categories = Category.objects.all()
            context = {
                'products': products,
                'categories': categories
            }
            return render(request, 'products/index.html', context)
        else:
            category_name = request.POST['category']
            category = Category.objects.get(name = category_name)
            products = Product.objects.filter(category = category)

            categories = Category.objects.all()
            context = {
                'products': products,
                'categories': categories
            }
            return render(request, 'products/index.html', context)



@login_required
def new_product(request):
    if request.method != 'POST':
        form = ProductForm()
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.owner = request.user
            new_product.save()
            
            return redirect('products:index')
        
    context = {'form': form}
    return render(request, 'products/new_product.html', context)
    

def product(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)


@login_required
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method != 'POST':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:product', product_id=product.id)

    context = {
        'product':product,
        'form':form
    }
    return render(request, 'products/update_product.html', context)


@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('products:index')


@login_required
def my_posts(request):
    products = Product.objects.all()
    my_products = []

    for product in products:
        if product.owner == request.user:
            my_products.append(product)
            
    context = {
        'my_products': my_products
    }
    return render(request, 'products/my_posts.html', context)


@login_required
def add(request, product_id):
    product = Product.objects.get(id=product_id)
    current_user = request.user
    product.cart.add(current_user)
    return redirect('products:product', product_id=product.id)


@login_required
def cart(request):
    current_user = request.user
    cart_products = current_user.cart.all()
    context = {
        'cart_products': cart_products
    }
    return render(request, 'products/cart.html', context)

@login_required
def order(request):
    return render(request, 'products/order.html')


def search(request):
    searched = request.POST['searched']
    all_products = Product.objects.all()
    result = []

    for product in all_products:
        if product.name.lower().startswith(searched.lower()):
            result.append(product)


    return render(request, 'products/index.html', {'products': result})



