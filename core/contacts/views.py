from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, JsonResponse
from django.views.generic import View
from django.views.generic.edit import CreateView

from core.contacts.models import Consultation, Contact  # type: ignore
from core.events.models.events import Event

from .forms import UserConsultationForm, UserContactForm


class ContactPage(CreateView):
    model = Contact
    form_class = UserContactForm
    template_name = 'pages/contact.html'

    def post(self, request, *args, **kwargs):
        form = UserContactForm(request.POST)

        print(self.get_form_class())
        if form.is_valid():
            # submit form based on either contact or consultation
            super(ContactPage, self).form_valid(form)

            # message
            messages.success(
                request, 'Message sent successfully. A representative would respond to your mail with 48hrs.'
            )

            return HttpResponsePermanentRedirect(self.request.path_info)

        #  Set object to None, since class-based view expects model record object
        self.object = None
        # message
        messages.error(request, 'Invalid Form Field(s). Kindly check field(s) and try again; all fields are required.')
        # Return class-based view form_invalid to generate form with errors
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date_published').all()[:3]
        return context


class ConsultView(View):

    def post(self, request, *args, **kwargs):
        form = UserConsultationForm(request.POST)

        if form.is_valid():
            # submit form
            Consultation.objects.create(**form.cleaned_data)

            return JsonResponse({
                'status':
                    'success',
                'message':
                    'Message sent successfully. A representative would respond to schedule a Consultation with 48hrs.'
            },)

        else:
            return JsonResponse({'status': 'error', 'message': form.errors},)
