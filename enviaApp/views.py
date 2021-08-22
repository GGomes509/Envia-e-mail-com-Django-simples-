from django import template
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_mail(mail,nome123):

    context={'mail':mail,'nome123':nome123}
    template = get_template('messagem.html')
    content =template.render(context)
    
    email = EmailMultiAlternatives(
        'Teste envio mensagem 30/07',
        'Gabri Gomes',
        settings.EMAIL_HOST_USER,
        [mail],
        cc=['O e-mail que envia um copia']

    )

    email.attach_alternative(content,'text/html')
    email.send()


def home(request):
    if request.method == "POST":
        mail= request.POST.get('mail')
        nome123= request.POST.get('nome123')


        send_mail(mail,nome123)
    return render(request,'home.html')
