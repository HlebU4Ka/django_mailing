from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MailingLog


# Представление для списка логов рассылки
class MailingLogListView(ListView):
    model = MailingLog
    template_name = 'mailinglog_list.html'
    context_object_name = 'mailinglogs'


# Представление для деталей лога рассылки
class MailingLogDetailView(DetailView):
    model = MailingLog
    template_name = 'mailinglog_detail.html'
    context_object_name = 'mailinglog'


# Представление для создания нового лога рассылки
class MailingLogCreateView(CreateView):
    model = MailingLog
    fields = ['mailing_message', 'datetime_last_attempt', 'status_attempt', 'server_response']
    template_name = 'mailinglog_form.html'

    def get_success_url(self):
        return reverse_lazy('mailinglog-detail', kwargs={'pk': self.object.pk})


# Представление для обновления данных лога рассылки
class MailingLogUpdateView(UpdateView):
    model = MailingLog
    fields = ['mailing_message', 'datetime_last_attempt', 'status_attempt', 'server_response']
    template_name = 'mailinglog_form.html'

    def get_success_url(self):
        return reverse_lazy('mailinglog-detail', kwargs={'pk': self.object.pk})


# Представление для удаления лога рассылки
class MailingLogDeleteView(DeleteView):
    model = MailingLog
    success_url = reverse_lazy('mailinglog-list')
    template_name = 'mailinglog_confirm_delete.html'
    context_object_name = 'mailinglog'
