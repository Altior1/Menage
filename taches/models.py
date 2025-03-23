from datetime import date
import datetime
import django
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField("Description de la tache si nécéssaire")
    created = models.DateTimeField(auto_now_add=True)
    timer= models.TimeField("Temps avant répétition")
    last_time_done = models.DateTimeField("Dernière fois que la tache a été effectuée", default=django.utils.timezone.now)

    def __str__(self):
        return self.title
    
    def is_to_do(self):
        return self.last_time_done < datetime.datetime.now() - self.timer