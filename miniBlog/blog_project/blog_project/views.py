from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'
