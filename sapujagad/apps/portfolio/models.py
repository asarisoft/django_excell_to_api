from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Portfolio(models.Model):
    img =  models.ImageField(upload_to=FilenameGenerator(
        prefix='portfolio'))
    img_detail =  models.ImageField(upload_to=FilenameGenerator(
        prefix='portfolio'))
    title = models.CharField(max_length=254, blank=True, null=True)
    sub_title = models.CharField(max_length=254, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
