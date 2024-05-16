from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Min, Max
from django.views.generic import ListView, DetailView
from .models import ProductModel, Category, ProductTag, ColorModel, BrandModel, SizeModel, Wishlist



class ShoppingCart(ListView):
    template_name = "shopping-cart.html"

    def get_queryset(self):
        products = ProductModel.get_cart_objects(self.request)
        return products
    

class Shop(ListView):
    template_name = "shop.html"
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.all()

        search = self.request.GET.get("search")
        if search:
            qs = qs.filter(title__icontains=search)#__icontains

        
        cat = self.request.GET.get("cat")
        if cat:
            qs = qs.filter(category_id=cat)


        tag = self.request.GET.get("tag")
        if tag:
            qs = qs.filter(tags=tag)


        size = self.request.GET.get("size")
        if size:
            qs = qs.filter(sizes=size)



        color = self.request.GET.get("color")
        if color:
            qs = qs.filter(colors=color)


        brand = self.request.GET.get("brand")
        if brand:
            qs = qs.filter(brand_id=brand)


        sort = self.request.GET.get("sort")
        if sort == "price":
            qs = qs.order_by("price")
        elif sort == "-price":
            qs = qs.order_by("-price")
        elif sort == "sale":
            qs = qs.filter(sale=True)


        price = self.request.GET.get('price')
        if price:
            min, max = price.split(";")
            qs = qs.filter(real_price__gte=min, real_price__lte=max)#__gte/__lte


        return qs 
    

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        data['tags'] = ProductTag.objects.all()
        data['sizes'] = SizeModel.objects.all()
        data['brands'] = BrandModel.objects.all()
        data['colors'] = ColorModel.objects.all()
        data['min_price'], data['max_price'] = ProductModel.objects.aggregate(Min("real_price"), Max("real_price")).values()
        return data
    



class ProductDetail(DetailView):
    model = ProductModel
    template_name = "shop-details.html"


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['products'] = ProductModel.objects.all().exclude(id=self.object.pk)[:4]
        return data
    

@login_required
def wishlist_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    Wishlist.created_or_delete(request.user, product)
    return redirect(request.GET.get("next", '/'))


class WishlistView(LoginRequiredMixin, ListView):
    template_name = "wishlist.html"

    def get_queryset(self):
        return ProductModel.objects.filter(wishlistmodel__user_id=self.request.user)

def update_cart_view(request, id):
    cart = request.session.get("cart", [])

    if id in cart:
        cart.remove(id)

    else:
        cart.append(id)


    request.session['cart'] = cart 
    print(request.session['cart'])
    return redirect(request.GET.get("next", '/'))
