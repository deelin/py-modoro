from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=1024*16)
    user = models.ForeignKey(User)
    pomodoros = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

'''
Timer States

We only need two: READY and STARTED

If READY -> You can start the timer. Move timer to STARTED
If STARTED -> After time finishes, increment pomodoro count.
              Move timer back to READY state

If you try to start a STARTED timer, you simply start the
time again and move to READY is it finishes.
'''

#STARTED = "STARTED"
#READY = "READY"

class Timer(models.Model):
    task = models.ForeignKey(Task)                                                                     
    timestamp = models.DateTimeField(auto_now_add=True)                                                
    #action = models.CharField(max_length=1, choices=TASK_RUN_ACTION_CHOICE)

