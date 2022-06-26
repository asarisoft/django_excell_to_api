from django.db import models

class Settings(models.Model):
    NAME = (
        ('url_save', 'url_save'),
    )
    name = models.CharField(max_length=50, choices=NAME, unique=True)
    text_value = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
