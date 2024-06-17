from orders.models import OrderHistory
from django import  forms

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = OrderHistory
        exclude = ['user', 'products', 'created_at']


