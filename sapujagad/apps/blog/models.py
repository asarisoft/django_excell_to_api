from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Blog(models.Model):
    img1 =  models.ImageField(upload_to=FilenameGenerator(
        prefix='banner'))
    img2 =  models.ImageField(upload_to=FilenameGenerator(
        prefix='banner'), blank=True, null=True)
    img3 =  models.ImageField(upload_to=FilenameGenerator(
        prefix='banner'), blank=True, null=True)
    title = models.CharField(max_length=254, blank=True, null=True)
    date = models.DateField()
    short_desc = models.CharField(max_length=254, blank=True, null=True)
    long_desc = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
