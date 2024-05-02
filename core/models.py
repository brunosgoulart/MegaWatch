from django.db import models
from datetime import datetime

# Create your models here.
class HDPO(models.Model):
    DjangoTimeStamp = models.DateTimeField(default=datetime.now())
    PowerActive = models.DecimalField(max_digits=10, decimal_places=2)
    PowerReactive = models.DecimalField(max_digits=10, decimal_places=2)
    Level = models.DecimalField(max_digits=10, decimal_places=3)
    Escape = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
def __str__(self):
    return self.name
