from itertools import count
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
import razorpay
from .models import OrderPlaced, Product, Customer, Cart, Payments, Whishlist
from urllib import request
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from app.forms import LoginForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
# Create your views here.

class Home(View):
    def get(self, request):
     #product=Product.objects.filter(title=val)
     category=Product.objects.values_list('category', flat=True).distinct()
     #print(category)
     totalitem=0
     if request.user.is_authenticated:
         totalitem=len(Cart.objects.filter(user=request.user))
     return render(request,"frontend/home.html", locals())
 
    
def Login(request):
    return render(request, "frontend/login.html")

class ProfileView(View):
    def get(self, request):
        form=CustomerProfileForm()
        return render(request, 'account/profile.html', locals())
    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            
            reg=Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations!!! Additional data has been added..')
        else:
            messages.error(request, 'Failed, Invalid input Data.')
        return render(request, 'account/profile.html', locals())
    
def address(request):
    if request.user.is_authenticated:
         totalitem=len(Cart.objects.filter(user=request.user))
    add=Customer.objects.filter(user=request.user)
    return render(request, 'account/address.html', locals())

class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form= CustomerProfileForm(instance=add)
        return render(request, 'account/updateaddress.html', locals())
    def post(self, request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,'Congratulations!!! Profile update successfully')
        else:
            messages.warning(request, 'Invalid Input Data')
        return redirect('address')

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values_list('category', flat=True).distinct()
        # print(product)     
        if request.user.is_authenticated:
         totalitem=len(Cart.objects.filter(user=request.user))
        return render(request, 'frontend/category.html',locals())
    
class ProductDetails(View):
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk)
        allproducts=Product.objects.all().order_by('-id')[:3][::-1]
        # whish=Whishlist.objects.filter(Q(product=product) & Q(user=request.user))
        # print(whish)
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request, 'frontend/product-details.html', locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form=CustomerRegistrationForm()
        return render(request, 'account/customer-registration.html', locals())
    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully")
        else:
            messages.error(request, "Invali input Data")
        return render(request, 'account/customer-registration.html', locals())
    
    
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('product_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    if request.user.is_authenticated:
         totalitem=len(Cart.objects.filter(user=request.user))
    return redirect('/cart')
    
def show_cart(request):
    user=request.user
    cart = Cart.objects.filter(user=user)
    if request.user.is_authenticated:
         totalitem=len(Cart.objects.filter(user=request.user))
    amount=0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount=amount+value
    totalamount=amount+40
    
    return render(request, 'frontend/addtocart.html', locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount=amount+value
        totalamount=amount+40
        
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
            
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount=amount+value
        totalamount=amount+40
        
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
            
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount=amount+value
        totalamount=amount+40
        
        data={
            'amount':amount,
            'totalamount':totalamount
            
        }
        return JsonResponse(data)
    
class checkout(View):
    def get(self, request):
        user=request.user
        add=Customer.objects.filter(user=user)
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount=amount+value
        totalamount=amount+40
        razorpayamount=int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data={"amount":razorpayamount,"currency":"INR","receipt":"order_rcptid_12"}
        payment_response=client.order.create(data=data)
        print(payment_response)
        #{'id': 'order_MSCHH0A8VeA34e', 'entity': 'order', 'amount': 54200, 'amount_paid': 0, 'amount_due': 54200, 'currency': 'INR', 'receipt': 'order_rcptid_12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1692507067}
        order_id= payment_response['id']
        order_status=payment_response['status']
        if order_status == "created":
            payment = Payments(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()
        # total=cart.quantity*cart.product.discounted_price
        if request.user.is_authenticated:
         totalitem=len(Cart.objects.filter(user=request.user))
        return render(request, 'frontend/checkout.html', locals())
    
def Payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    user=request.user
    #To update payment status and payment id
    customer=Customer.objects.get(id=cust_id)
    payment=Payments.objects.get(razorpay_order_id=order_id)
    payment.paid=True
    payment.razorpay_payment_id=payment_id
    payment.save()
    
    #To save order details
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()
    return redirect("orders")
    
def orders(request):
    order=OrderPlaced.objects.filter(user=request.user)
    print(order)
    return render(request, 'account/orders.html', locals())
    
# def base(View):
#     def get(self, request):
#         user=request.user
#         cart=Cart.objects.filter(user=user)
#         return render(request, 'frontend/base.html', locals())

def logout_view(request):
    logout(request)
    return redirect('home')

