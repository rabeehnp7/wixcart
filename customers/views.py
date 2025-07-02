from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from . models import Customer,Address
from django.contrib import messages

# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        try:
            context['register']=True
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            address=request.POST.get('address')

            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            customer=Customer.objects.create(
                user=user,
                phone=phone,
            )
            address_new=Address.objects.create(
                  customer=customer,
                  address=address          
            )
            messages.success(request,"User registered successfully")
        except Exception as e:
            error_message="Username already exists or invalid inputs"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message="Invalid credentials"
            messages.error(request,error_message)

    return render(request,'account.html',context)

def sign_out(request):
    logout(request)
    return redirect('home')
