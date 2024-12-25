from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    
def get_success_url(self):
        # Redirect to the client page after login
        return reverse_lazy('clients_page') 

@login_required
def clients_page(request):
    return render(request, 'clients_page.html')


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

@login_required
def profile(request):
    return render(request, 'profile.html')



class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('profile')