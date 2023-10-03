from django.db import models
from myproject.message_app.models import MailingMessage


class MailingManager(models.Manager):
    def started_mailings(self):
        return self.filter(status='started')


class Mailing(models.Model):
    send_time = models.TimeField()
    frequency_choices = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]
    frequency = models.CharField(max_length=20, choices=frequency_choices)
    status_choices = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)

    messages = models.ManyToManyField(MailingMessage, related_name='mailings', blank=True)

    objects = MailingManager()

    def __str__(self):
        return f'Mailing - {self.id}'
