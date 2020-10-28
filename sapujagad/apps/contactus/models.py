from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Contactus(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=25, blank=True, null=True)
    message = models.TextField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name
