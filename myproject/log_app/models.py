from django.db import models
from myproject.message_app.models import MailingMessage


class MailingLog(models.Model):
    mailing_message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE)
    datetime_last_attempt = models.DateTimeField()
    status_attempt = models.CharField(max_length=50)
    server_response = models.TextField()

    def __str__(self):
        return f'Лог рассылки - {self.mailing_message.subject} ({self.datetime_last_attempt})'
