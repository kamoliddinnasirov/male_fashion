from django.urls import path
from shop.views import Shop, ProductDetail, WishlistView, update_cart_view, ShoppingCart, wishlist_view

app_name = "shop"

urlpatterns = [
    path("", Shop.as_view(), name="home"),
    path("product/<int:pk>", ProductDetail.as_view(), name="detail"),
    path("product/<int:pk>/wishlist/", wishlist_view, name="wishlist"),
    path("wishlist/", WishlistView.as_view(), name='all_wishlist'),
    path("add_cart/<int:id>/", update_cart_view, name="cart"),
    path("shopping_cart/", ShoppingCart.as_view(), name="shopping_cart" )

]