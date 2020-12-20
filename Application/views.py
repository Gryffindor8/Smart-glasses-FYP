from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .form import *
from .models import *


def loginTest(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.POST['username'])
        print( request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password was incorrect!')

    return render(request, 'Application/login.html')


def signup(request):
    form = RegisterUser()
    if request.method == "POST":
        form = RegisterUser(request.POST)
        print('-------------------form print-----------------')
        print(form)
        Productid = ProductID.objects.all()
        pid = request.POST['pid']
        idexist = False
        ProdExist = False

        ## check if the Product id is exist
        for x in Productid:
            if x.Productid == pid:
                idexist = True
        
        ## check if the product is not register already
        if idexist == True:
            alreadyExist = CustomerProd.objects.all()
            print('------------------------------------')
            print(alreadyExist)
            for exist in alreadyExist:
                temp = str(exist)
                if temp == pid:
                    ProdExist = True
                    messages.info(request, 'One user is already register with this Product Id')

        if ProdExist == True:
            print("one user is already register that product ")
        else:
            if form.is_valid():
                instance = form.save()
                # print(instance.pk)
                print('------------------------------------')
                ##instance.User = request.user
                user = form.cleaned_data.get("username")

                p = ProductID.objects.get(Productid=request.POST['pid'])
                print('------------------------------------')
                print("asd" ,p)
                CustomerProd.objects.create(User=User.objects.get(id=instance.pk), customerid=p)
                return redirect('login')
            else:
                messages.info(request, 'This Username Already exist!')
                print("user already exit ")
    context = {'form': form}
    return render(request, 'Application/signup.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'Application/Deshboard.html')
