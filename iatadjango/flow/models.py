from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.CharField(max_length=120)
    source = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    date = models.DateField()
    pnr = models.CharField(max_length=10)

    def __str__(self):
        return self.flight
