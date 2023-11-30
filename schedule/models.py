from django.db import models

from accounts.models import CustomUser

class ScheduleRegister(models.Model):
    
    user = models.ForeignKey(
        CustomUser,
        verbose_name='user',
        on_delete=models.CASCADE
    )
    
    date = models.DateField(
        verbose_name='date'
    )
    
    event = models.TextField(
        verbose_name='event'
    )
    
    place = models.CharField(
        verbose_name='place',
        max_length=200
    )

    
    def __str__(self):
        return self.event
    
