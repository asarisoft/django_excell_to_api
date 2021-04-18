from django.db import models

from nxp.core.utils import FilenameGenerator


class Dealer(models.Model):
    code = models.CharField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
