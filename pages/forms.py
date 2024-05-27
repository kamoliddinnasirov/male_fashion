from django import forms 
from pages.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['created_at']