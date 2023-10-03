from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MailingMessage


# Представление для списка сообщений рассылки
class MailingMessageListView(ListView):
    model = MailingMessage
    template_name = 'mailingmessage_list.html'
    context_object_name = 'mailingmessages'


# Представление для деталей сообщения рассылки
class MailingMessageDetailView(DetailView):
    model = MailingMessage
    template_name = 'mailingmessage_detail.html'
    context_object_name = 'mailingmessage'


# Представление для создания нового сообщения рассылки
class MailingMessageCreateView(CreateView):
    model = MailingMessage
    fields = ['mailing', 'subject', 'body']
    template_name = 'mailingmessage_form.html'

    def get_success_url(self):
        return reverse_lazy('mailingmessage-detail', kwargs={'pk': self.object.pk})


# Представление для обновления данных сообщения рассылки
class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    fields = ['mailing', 'subject', 'body']
    template_name = 'mailingmessage_form.html'

    def get_success_url(self):
        return reverse_lazy('mailingmessage-detail', kwargs={'pk': self.object.pk})


# Представление для удаления сообщения рассылки
class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailingmessage-list')
    template_name = 'mailingmessage_confirm_delete.html'
    context_object_name = 'mailingmessage'
