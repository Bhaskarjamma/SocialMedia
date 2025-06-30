
from django.urls import path,include
from acoounts.views import SignUpView, HomeView,user_logout
from django.contrib.auth.views import LoginView
from acoounts.forms import LoginForm

app_name = 'acoounts'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name = 'accounts/login.html',authentication_form = LoginForm), name='login'),
    path('logout/', user_logout, name='logout'),
]