from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm


def submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['your_email@gmail.com'],
            )
            return render(request, 'form_contact/partial.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'form_contact/partial.html', {'form': form})
