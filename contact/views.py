from django.shortcuts import render

from django.core.mail import BadHeaderError
from django.http import HttpResponse

from .forms import ContactMe
from django.core.mail import send_mail

from django.contrib import messages


def contact(request):

    form = ContactMe()
    if request.method == 'POST':
        form = ContactMe(request.POST)
        from_name = str(form['name'].value())
        from_email = str(form['email'].value())
        subject = str(form['subject'].value())
        message = str(form['message'].value()) + f'\nfrom :name: {from_name} email: {from_email}'

        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['f.benayad95@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, f'Your email has been sent successfully to Company')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    context = {
        'title': 'Contact',
        'form': form,
    }

    return render(request, 'contact/contact.html', context)