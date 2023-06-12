from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name *", max_length=30, required=True)
    email = forms.EmailField(label="Email *", max_length=50, required=True)
    subject = forms.CharField(label="Subject *", max_length=80, required=True)
    message = forms.CharField(label="Message *", widget=forms.Textarea, required=True)