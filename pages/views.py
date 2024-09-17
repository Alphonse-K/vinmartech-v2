from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from pages.models import Message

from pages.forms  import MessageForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'pages/index.html'


class TeamView(TemplateView):
    template_name = 'pages/team.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(CreateView):
    model = Message
    template_name = 'pages/contact.html'
    form_class = MessageForm
    success_url = 'pages:home'

    def form_valid(self, form):
        form.save()  # Save the form data to the database
        
        # Prepare the context with success message and person data
        context = self.get_context_data(form=form)
        context['message'] = 'Merci de votre message!'
        
        return self.render_to_response(context)
    
    # Optionally, form_invalid method can also be handled if needed
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)        