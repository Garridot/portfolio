from django.urls import path
from . import views

urlpatterns = [    
    path('',views.MainView.as_view()),   
    path('send_email/',views.EmailSend,name='send_email')
] 