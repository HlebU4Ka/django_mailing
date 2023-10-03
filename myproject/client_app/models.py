from django.db import models
from myproject.mailing_app.models import Mailing


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField()

    mailings = models.ManyToManyField(Mailing, related_name='clients', blank=True)

    def __str__(self):
        return self.email
