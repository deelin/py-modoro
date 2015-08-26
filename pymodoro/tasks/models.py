from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=1024*16)
    user = models.ForeignKey(User)
    pomodoros = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
