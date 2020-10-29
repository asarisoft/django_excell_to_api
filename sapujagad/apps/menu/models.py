from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=254)
    order = models.IntegerField(default=0)
    one_page_url = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name