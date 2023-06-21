from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'authentication_app/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'authentication_app/signup.html', {'form': form})

def logout_session(request):
    logout(request)
    return redirect('Home')

def login_session(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Incorrect information.')
    form = AuthenticationForm()
    return render(request, 'authentication_app/login.html', {'form': form})