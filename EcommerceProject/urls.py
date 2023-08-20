"""
URL configuration for EcommerceProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from EcommerceProject import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from app.forms import LoginForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.Home.as_view(), name="home"),
    path("login/",views.Login, name="login" ),
    path("logout/",views.logout_view, name="logout" ),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('product-details/<int:pk>', views.ProductDetails.as_view(), name='product-details'),
    
    #cart
    path('add-to-cart/', views.add_to_cart, name="add-to-cart"),
    path('cart/', views.show_cart, name="showcart"),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),    
    path('paymentdone/', views.Payment_done, name="paymentdone"),
    path('orders/', views.orders, name="orders"),
    
    # customer 
    path('resgistration/', views.CustomerRegistrationView.as_view(), name='registration'),
    path('account/login', LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm),name='login' ),
    path('account/profile/', views.ProfileView.as_view(), name='profile'),
    path('account/address', views.address, name='address'),
    path('account/updateaddress/<int:pk>', views.UpdateAddress.as_view(), name='updateaddress'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

