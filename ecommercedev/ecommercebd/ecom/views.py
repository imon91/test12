import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

# Admin Dashboard
from ecom.models import Order
from ecomadminapp.models import ProductCategory
from ecomadminapp.models import Product
from registration.models import CompanyRegistration


def index(request):
    context = dict()
    context['products'] = Product.objects.filter(is_active=True).order_by('-id')
    return render(request, 'ecom/display.html', context)


def product_detail(request, id):
    context = dict()
    context['product_details'] = get_object_or_404(Product, pk=id)
    return render(request, 'ecom/product_detail.html', context)


def addcart(request):

    product = Product.objects.get(pk=request.GET.get('product_id'))
    quantity = request.GET.get('quantity')
    request.session['product'] = "product"
    request.session['quantity'] = "quantity"

    return HttpResponse("Added cart successfully..  ! ")
