from sapujagad.core.utils import FilenameGenerator
from django.db import models

class Pricing(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField()
    desc_list = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
