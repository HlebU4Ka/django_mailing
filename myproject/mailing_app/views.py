from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mailing


# Представление для списка рассылок
class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_list.html'
    context_object_name = 'mailings'


# Представление для деталей рассылки
class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing_detail.html'
    context_object_name = 'mailing'


# Представление для создания новой рассылки
class MailingCreateView(CreateView):
    model = Mailing
    fields = ['send_time', 'frequency', 'status']
    template_name = 'mailing_form.html'

    def get_success_url(self):
        return reverse_lazy('mailing-detail', kwargs={'pk': self.object.pk})


# Представление для обновления данных рассылки
class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['send_time', 'frequency', 'status']
    template_name = 'mailing_form.html'

    def get_success_url(self):
        return reverse_lazy('mailing-detail', kwargs={'pk': self.object.pk})


# Представление для удаления рассылки
class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing-list')
    template_name = 'mailing_confirm_delete.html'
    context_object_name = 'mailing'
