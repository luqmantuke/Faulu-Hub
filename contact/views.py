from django.shortcuts import render, reverse
from .models import *
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def contactView(request):

    form_class = ContactForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = form.cleaned_data['message']
            contact_message = f'Customer  "{name}" with the email {email} just contacted you and left a message  "{message}" please contact him as soon as possible'
            form.save()
            #try: 
               #send_mail(subject, contact_message, settings.EMAIL_HOST_USER, ['tuksim@tuksimadventures.com'], settings.FAIL_SILENTLY)
            #except BadHeaderError:
                #return HttpResponse('Invalid Header.')
            
            messages.success(request, f"Thank You For Contacting Us { name }, We Shall Reach You As Soon As Possible. :)")
            return HttpResponseRedirect(reverse('home'))
            
        else:
            form = ContactForm()
        
    return render(request, 'contact/contact.html', {'form': form})
