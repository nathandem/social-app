from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "index.html"

# the idea is to put the home page in the project folder,
# so that it's independent from the apps

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
