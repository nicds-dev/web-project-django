from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    return render(request, 'contact_app/contact.html', {'contact_form': contact_form})