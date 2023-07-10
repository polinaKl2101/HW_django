from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import MailingForm
from catalog.models import Mailing
from catalog.services import send_mail


class MailingListView(LoginRequiredMixin, generic.ListView):
    model = Mailing
    template_name = 'catalog/mailing/mailing_list.html'
    extra_context = {
        'title': 'Список рассылок'
    }


class MailingCreateView(generic.CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'catalog/mailing/mailing_form.html'
    success_url = reverse_lazy('catalog:mailing')

    def form_valid(self, form):
        form.instance.status = 'started'
        response = super().form_valid(form)
        send_mail(self.object)
        return response

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        message = self.object
        message.status = 'started'
        message.save()
        send_mail(message)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailing_number'] = Mailing.objects.count()
        return context


class MailingDetailView(generic.DetailView):
    model = Mailing
    template_name = 'catalog/mailing/mailing_detail.html'


class MailingUpdateView(generic.UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'catalog/mailing/mailing_update.html'
    success_url = reverse_lazy('catalog:mailing')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('catalog:mailing_update', kwargs={'pk': pk})


class MailingDeleteView(generic.DeleteView):
    model = Mailing
    template_name = 'catalog/mailing/mailing_confirm_delete.html'
    success_url = reverse_lazy('catalog:mailing')
