from django.db import models

from nxp.core.utils import FilenameGenerator


class Product(models.Model):
    serial_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
