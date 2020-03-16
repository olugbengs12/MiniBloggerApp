from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# from django.core.mail import send_mail
# from django.conf import settings

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


# def index(request):

# 	if request.method == 'POST':
# 		message = request.POST['message']

# 		send_mail('Sign Up',
# 		 message, 
# 		 settings.EMAIL_HOST_USER,
# 		 ['gbengaowoeye43@gmail.com'], 
# 		 fail_silently=False)
# 	return render(request, 'accounts/signup.html')