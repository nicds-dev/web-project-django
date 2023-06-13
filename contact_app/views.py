from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            try:
                send_mail(subject, f'The user with name {name} sent the following message:?\n\n {message}', email, ['cuentaparaadobe2001@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/contact/?valid')

    return render(request, 'contact_app/contact.html', {'contact_form': contact_form})