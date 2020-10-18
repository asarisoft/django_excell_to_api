from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Service(models.Model):
    img =  models.ImageField(upload_to=FilenameGenerator(
        prefix='service'))
    desc = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
