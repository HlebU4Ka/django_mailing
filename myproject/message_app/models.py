from django.db import models
from myproject.mailing_app.models import Mailing


class MailingMessage(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    logs = models.ManyToManyField(Mailing, related_name='messages', blank=True)

    def __str__(self):
        return self.subject
