
from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.shop,name='shop'),
    path('wishlist/',views.wishlist,name='whishlist'),
    path('singleproduct/',views.singleproduct,name='singleproduct'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
]
