from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Testimoni(models.Model):
    testimony = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.testimony