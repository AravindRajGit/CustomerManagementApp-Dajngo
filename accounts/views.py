from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import OrderForm,CreateUserForm,CustomerForm

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_users,allowed_users,admin_only

#With Autentication


#Registration Page
@unauthenticated_users
def registerPage(request):
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            print(form.errors)
            if form.is_valid():
                user=form.save();
                group=Group.objects.get(name='customer')
                user.groups.add(group)
                username=form.cleaned_data.get('username')
                messages.success(request,"Account Creted for"+" "+username)
                return redirect('Login')
        context={'form':form}
        return render(request,'accounts/register.html',context)


#Loginpage
@unauthenticated_users
def LoginPage(request):
        if request.method=='POST':
            username=request.POST.get("txtUsername")
            password=request.POST.get("txtPassword")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return  redirect('home')
            else:
               return HttpResponse("Invalid")
        return render(request,'accounts/login.html')



#AdminHomePage
@login_required(login_url='Login')
@admin_only
def Home(request):
    orders=Order.objects.all();
    customers=Customer.objects.all();
    total_orders=orders.count();
    totalorders=orders.count();
    delivered=orders.filter(status='Delivered').count();
    pending=orders.filter(status='Pending').count();
    OutofDelivery=orders.filter(status='Out of Delivery').count();
    context={'orders':orders,'customers':customers,'delivered_order':delivered,'peding_order':pending,'total_orders':totalorders,'Out_of_Delivery':OutofDelivery}
    return render(request,'accounts/dashboard.html',context)


#UserHomePage
def userpage(request):
    customerOrder=request.user.customer.order_set.all();
    totalorders=customerOrder.count();
    delivered=customerOrder.filter(status='Delivered').count();
    pending=customerOrder.filter(status='Pending').count();
    OutofDelivery=customerOrder.filter(status='Out of Delivery').count();
    context={'orders':customerOrder,'delivered_order':delivered,'peding_order':pending,'total_orders':totalorders,'Out_of_Delivery':OutofDelivery}
    return render(request,"accounts/customerhomepage.html",context)


#UserProfileSettings
@login_required(login_url='Login')
@allowed_users(allowed_roles=['customer'])
def customersettings(request):
    customerData=request.user.customer
    form=CustomerForm(instance=customerData)
    print(form)
    context={'form':form}
    return render (request,'accounts/custommer_settings.html',context)

#UserProfile
@login_required(login_url='Login')
@allowed_users(allowed_roles=['customer'])
def userprofile(request):
    customerOrder=request.user.customer.order_set.all();
    totalorders=customerOrder.count();
    delivered=customerOrder.filter(status='Delivered').count();
    pending=customerOrder.filter(status='Pending').count();
    OutofDelivery=customerOrder.filter(status='Out of Delivery').count();
    context={'orders':customerOrder,'delivered_order':delivered,'peding_order':pending,'total_orders':totalorders,'Out_of_Delivery':OutofDelivery}
    return render(request,"accounts/customer.html",context)


#ProductManagement
@login_required(login_url='Login')
@admin_only
def Products(request):
    orders=Order.objects.all();
    customers=Customer.objects.all();
    total_orders=orders.count();
    totalorders=orders.count();
    delivered=orders.filter(status='Delivered').count();
    pending=orders.filter(status='Pending').count();
    OutofDelivery=orders.filter(status='Out of Delivery').count();
    products=Product.objects.all();
    return render(request,"accounts/products.html",{'products':products,'delivered_order':delivered,'peding_order':pending,'total_orders':totalorders,'Out_of_Delivery':OutofDelivery})


#CustomersList
@login_required(login_url='Login')
@admin_only
def Customers(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    orders_count=orders.count();
    context={'customer':customer,'orders':orders,'orders_count':orders_count}
    return render(request,'accounts/customer.html',context)


#CreateOrders
@login_required(login_url='Login')
@unauthenticated_users
# @admin_only
def CreateOrder(request):
    form=OrderForm()
    if request.method== 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
    context={'form':form}
    return render(request,'accounts/order_form.html',context)


#UpdateOrders
@login_required(login_url='Login')
# @admin_only
@unauthenticated_users
def UpdateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/order_form.html',context)

@login_required(login_url='Login')
# @admin_only
@unauthenticated_users
def DeleteOrder(request,pk):
    order=Order.objects.get(id=pk);
    if request.method=='POST':
        order.delete();
        return redirect("/")
    context={'item':order}
    return render(request,"accounts/order_delete.html",context)

def LogOutUser(request):
    logout(request)
    return redirect('Login')





    
   
