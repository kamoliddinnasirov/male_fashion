from django.urls import path 
from pages.views import HomePage, ContacView


app_name = 'pages'

urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path("contact/", ContacView.as_view(), name='contact'),
]