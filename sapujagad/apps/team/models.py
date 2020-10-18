from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Team(models.Model):
    img =  models.ImageField(upload_to=FilenameGenerator(
        prefix='team'))
    name = models.CharField(max_length=254, blank=True, null=True)
    position = models.CharField(max_length=254, blank=True, null=True)
    motto = models.CharField(max_length=254, blank=True, null=True)
    fb_link = models.CharField(max_length=254, blank=True, null=True)
    twitter = models.CharField(max_length=254, blank=True, null=True)
    linkedin = models.CharField(max_length=254, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
