from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import datetime


# for company registration
def index(request):
    context = dict()
    pass

    # if request.method == "POST":
    #     name = request.POST['name']
    #     password = request.POST['password']
    #     email = request.POST['email']
    #     bank_account = request.POST['bank_account']
    #     contact_number = request.POST['contact_number']
    #     image = request.FILES['image']
    #     descriptions = request.POST['descriptions']
    #     contact_person = request.POST['Contact_Person']
    #     address = request.POST['address']
    #     username = email.split("@")[0]
    #     user_id = create_user(username, email, password)
    #
    #     company = CompanyRegistration(name=name, email=email, bank_account=bank_account, contact_number=contact_number,
    #                                   image=image, descriptions=descriptions,contact_person=contact_person,
    #                                   address=address, user=user_id,
    #                                   is_active=True, created=datetime.datetime.now()
    #                                   )
    #     company.save()
    #     context['msg'] = "You Successfully registered"
    #     return render(request, 'registration/login.html', context)
    #
    # return render(request, 'registration/registration.html')


def login(request):
    return render(request, 'registration/login.html')


def create_user(username, email, password):
    user = User(username=username,
                is_superuser=False,
                is_active=True,
                is_staff=False,
                email=email,
                date_joined=datetime.datetime.now())
    user.save()
    user.set_password(password)

    group = Group.objects.get(name='company')

    user.groups.add(group)
    user.save()
    return user


def password_update(request):
    context = dict()
    return redirect("registration:login")
