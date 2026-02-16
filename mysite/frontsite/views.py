from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'frontsite/index.html')

def hello(request):
    return render(request, 'frontsite/partials/hello.html')

def contact(request):
    context = _handle_contact_form(request)
    return render(request, 'frontsite/contact.html', context)

def contact_form(request):
    context = _handle_contact_form(request)
    return render(request, 'frontsite/partials/contact-form.html', context)

def _handle_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['your_email@gmail.com'],
            )
            return {'form': ContactForm(), 'success': True}
    else:
        form = ContactForm()
    return {'form': form}

def menu(request):
    return render(request, 'frontsite/partials/menu.html')

def mobile_menu(request):
    return render(request, 'frontsite/partials/mobile-menu.html')
