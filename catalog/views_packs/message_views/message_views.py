from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import MessageForm
from catalog.models import Message


class MessageListView(LoginRequiredMixin, generic.ListView):
    model = Message
    template_name = 'catalog/message/message_list.html'
    extra_context = {
        'title': 'Список сообщений'
    }


class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'catalog/message/message_form.html'
    success_url = reverse_lazy('catalog:message')


class MessageUpdateView(generic.UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'catalog/message/message_detail.html'
    success_url = reverse_lazy('catalog:message')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('catalog:message_update', kwargs={'pk': pk})


class MessageDeleteView(generic.DeleteView):
    model = Message
    template_name = 'catalog/message/message_confirm_delete.html'
    success_url = reverse_lazy('catalog:message')
