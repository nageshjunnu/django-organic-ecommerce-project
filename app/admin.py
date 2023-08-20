from django.contrib import admin
from .models import Product, Customer, Cart, Payments, OrderPlaced, Whishlist

# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display=["id", 'title', 'discounted_price', 'category', 'product_image']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']
    
@admin.register(Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display=['id', 'user', 'product', 'quantity']
    
@admin.register(Payments)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status', 'razorpay_payment_id', 'paid']
    
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']
    
@admin.register(Whishlist)
class WhishListAdminModel(admin.ModelAdmin):
    list_display=['id', 'user', 'product']