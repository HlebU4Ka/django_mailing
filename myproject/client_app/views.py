from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client


# Представление для списка клиентов
class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'  # Имя шаблона для отображения списка клиентов
    context_object_name = 'clients'  # Имя переменной контекста для передачи в шаблон


# Представление для деталей клиента
class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'  # Имя шаблона для отображения деталей клиента
    context_object_name = 'client'  # Имя переменной контекста для передачи в шаблон


# Представление для создания нового клиента
class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'full_name', 'comment']  # Поля, которые будут отображаться в форме создания клиента
    template_name = 'client_form.html'  # Имя шаблона для отображения формы создания клиента

    def get_success_url(self):
        return reverse_lazy('client-detail', kwargs={
            'pk': self.object.pk})  # После успешного создания, перейти к деталям созданного клиента


# Представление для обновления данных клиента
class ClientUpdateView(UpdateView):
    model = Client
    fields = ['email', 'full_name', 'comment']  # Поля, которые будут отображаться в форме обновления клиента
    template_name = 'client_form.html'  # Имя шаблона для отображения формы обновления клиента

    def get_success_url(self):
        return reverse_lazy('client-detail', kwargs={
            'pk': self.object.pk})  # После успешного обновления, перейти к деталям обновленного клиента


# Представление для удаления клиента
class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client-list')  # После успешного удаления, перейти к списку клиентов
    template_name = 'client_confirm_delete.html'  # Имя шаблона для подтверждения удаления клиента
    context_object_name = 'client'  # Имя переменной контекста для передачи в шаблон
