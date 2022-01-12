from django.shortcuts import redirect, render

from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib import messages
from portofolio.settings import EMAIL_HOST_USER
# Create your views here.

class MainView(TemplateView):
    template_name = "main.html"


def EmailSend(request):
    email   = request.POST['email']    
    message = request.POST['message']   

    send_mail(
        f'Portfolio Message:{email}',
        message,
        email,
        [EMAIL_HOST_USER,],        
    )
    messages.success(request,'Gracias! Tratare de responder lo mas rapido que sea posible. ')
    return redirect('http://127.0.0.1:8000/#contact')
    


