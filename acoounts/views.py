from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.views import LogoutView
# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('acoounts:home')
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect(self.success_url)

class IndexView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/app/home/')
        return render(request, 'index.html')
class HomeView(TemplateView):
    template_name = 'accounts/home.html'

def user_logout(request):
    logout(request)
    return redirect('index')
