from nxp.core.utils import FilenameGenerator
from django.db import models


class Settings(models.Model):
    TYPE = (
        ('seo_description', 'SEO Description'),
        ('seo_title', 'SEO Title'),
        ('seo_keywords', 'SEO Keywords'),
        ('seo_image', 'SEO Image'),
        ('seo_fb_id', 'SEO FbID'),
    )
    name = models.CharField(max_length=254, choices=TYPE, unique=True)
    text_value = models.TextField(blank=True, null=True)
    img_value =  models.ImageField(upload_to=FilenameGenerator(
        prefix='settings'), blank=True, null=True)

    def __str__(self):
        return self.name
