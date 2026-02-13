from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'frontsite/index.html')

def hello(request):
    return render(request, 'frontsite/partials/hello.html')

def contact(request):
    return render(request, 'frontsite/contact.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                subject=f"Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['your_email@gmail.com'],  # Replace with the email you want to receive messages at
            )
            # Reset form and indicate success
            return render(request, 'frontsite/partials/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'frontsite/partials/contact.html', {'form': form})