from django.shortcuts import redirect, render

from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

class MainView(TemplateView):
    template_name = "main.html"




