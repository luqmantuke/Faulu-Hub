from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta(object):
        model = Contact
        fields = ('__all__')
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder' : 'Your message...'}),
        }