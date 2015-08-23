from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=1024*16)
    total_time = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

