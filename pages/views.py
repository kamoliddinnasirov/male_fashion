from typing import Any
from django.shortcuts import render
from pages.forms import ContactForm
from pages.models import Banner, MainSM, MainSMImage
from django.views.generic import TemplateView, CreateView
from blog.models import Post
from django.urls import reverse


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['posts'] = Post.objects.order_by("-pk")[:3]
        data['banners'] = Banner.objects.filter(is_active=True).order_by("-id")
        data['medias'] = MainSM.objects.all()
        data['images'] = MainSMImage.objects.all()
        return data
    


class ContacView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse("pages:contact")



