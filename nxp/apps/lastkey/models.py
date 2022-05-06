from django.db import models

class LastKey(models.Model):
    last_key = models.CharField(max_length=100)
   
    def __str__(self):
        return f"{self.last_key}"

