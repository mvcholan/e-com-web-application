from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('register',views.register, name="register"),
    path('remove_cart/<str:cid>',views.remove_cart, name="remove_cart"),
    path('login',views.loginview, name="login"),
    path('cartview',views.cart_view, name="cartview"),
    path('logout',views.logoutview, name="logout"),
    path('collection',views.collection, name="collection"),
    path('collection/<str:name>',views.collectionsview, name="collection"),
    path('collection/<str:cname>/<str:pname>',views.product_details, name="product_details"),
    path('addtocart',views.add_to_cart, name="addtocart"),
    path('addtofav',views.fav_page, name="addtofav"),
    path('fav',views.fav_view, name="fav"),
    path('remove_fav/<str:fid>',views.remove_fav, name="remove_fav"),

]
