from django.shortcuts import render, HttpResponse

# Create your views here.

def authentication(request):
    return render(request, 'authentication_app/login.html')