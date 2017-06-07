from django.db import models
from django.utils import timezone
from datetime import datetime

class Thing(models.Model):
    quitter = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    quit_date = models.DateTimeField(default=timezone.now)
    cost_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField()
    
    @property
    def timesince(self):
        "Time since quit date"
        now = timezone.now() 
        then = self.quit_date
        return  (now - then).days
    
    @property
    def savings(self):
        "Savings since quitting"
        return self.timesince * self.cost_per_day

    def quit_now(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


        

    
    
        
