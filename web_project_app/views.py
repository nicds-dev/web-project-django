from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'web_project_app/index.html')

def about(request):
    return render(request, 'web_project_app/about.html')