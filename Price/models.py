from django.db import models

class Currency(models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=20,default="")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name