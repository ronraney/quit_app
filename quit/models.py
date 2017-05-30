from django.db import models
from django.utils import timezone


class Thing(models.Model):
    quitter = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    quit_date = models.DateTimeField(
            default=timezone.now)
    cost_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField()

    def quit_now(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
