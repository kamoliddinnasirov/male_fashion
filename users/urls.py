from django.urls import  path
from users.views import logout_veiw, login_view, user_registration, ProfileView


app_name = 'user'


urlpatterns = [
    path("profile/", ProfileView.as_view(), name='profile'),
    path("logout/", logout_veiw, name='logout'),
    path("login/", login_view, name='login'),
    path("registration/", user_registration, name='registration')
]