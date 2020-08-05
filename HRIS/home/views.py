from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
#admin1234, halumhalum

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")

    #Customer Table
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    #place order table
    products = Product.objects.all()



    context ={
        'customers':customers, 'orders': orders,
        'total_orders':total_orders, 'delivered':delivered,
        'pending':pending,  'products': products

    }

    
    return render(request, 'index.html', context)

def loginUser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')

        else:
            # No backend authenticated the credentials
            return render(request, 'loginUser.html')
            


    return render(request, 'loginUser.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
