from django.shortcuts import render, reverse, redirect
from orders.forms import CheckoutForm
from orders.models import OrderHistory
from django.views.generic import ListView, CreateView
from shop.models import ProductModel
from django.db.models import Sum


class CheckoutView(CreateView):
    model = OrderHistory
    template_name = 'checkout.html'
    form_class = CheckoutForm
    success_url = "order/history/"


    def dispatch(self, request, *args, **kwargs):
        if len(request.session.get('cart', [])) == 0:
            return redirect(reverse('pages:home'))
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return reverse("orders:history")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = ProductModel.get_cart_objects(self.request)

        if hasattr(self.request.user, 'profiles'):
            context['profile'] = self.request.user.profiles

        return context

    def form_valid(self, form):
        products = ProductModel.get_cart_objects(self.request)
        price = products.aggregate(Sum("real_price")).get("real_price_sum", '')

        order = form.save(commit=True)

        if self.request.user.is_authenticated:
            order.user_id = self.request.user.id

        order.total_price = price
        order.products.set(products)
        order.save()

        self.request.session['cart'] = []
        return super().form_valid(form)


class OrderHistoryView(ListView):
    template_name = 'order_history.html'

    def get_queryset(self):
        return  OrderHistory.objects.filter(user=self.request.user.id)
