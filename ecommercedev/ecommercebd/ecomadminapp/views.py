from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

# Admin Dashboard
from ecomadminapp.models import ProductCategory
from registration.models import CompanyRegistration


@login_required
def index(request):
    context = dict()
    context['total_company'] = CompanyRegistration.objects.filter(is_active=True).count()
    return render(request, 'ecomadminapp/dashboard.html', context)


@login_required
def product_category(request):

    context = dict()
    context['products'] = ProductCategory.objects.filter(is_active=True).order_by('-id')
    if request.method == "POST":
        name = request.POST['name']
        descriptions = request.POST['descriptions']
        image = request.FILES['image']

        category = ProductCategory(name=name, image=image,descriptions=descriptions, is_active=True)
        category.save()
        context['msg']="successfully save"
    return render(request, 'ecomadminapp/product_category.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('ecomadminapp:index')
    else:
        if request.method == "POST":
            user = request.POST['user']
            password = request.POST['password']
            auth = authenticate(request, username=user, password=password)

            if auth is not None:
                auth_login(request, auth)
                return redirect('ecomadminapp:index')
            else:
                msg = "Please check your user name or password"
                context = {
                    'msg': msg,
                }
                return render(request, 'ecomadminapp/login.html', context)

    return render(request, 'ecomadminapp/login.html')


def logout(request):
    auth_logout(request)
    logoutmsg = 'your are successfully logout'
    context = {
        'logoutmsg': logoutmsg,
    }
    return render(request, 'ecomadminapp/login.html', context)


def company_detail(request):
    context = dict()
    context['total_company'] = CompanyRegistration.objects.filter(is_active=True).order_by('-id')
    return render(request, 'ecomadminapp/companylist.html', context)
