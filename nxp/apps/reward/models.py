from nxp.core.utils import FilenameGenerator, custom_slugify
from django.db import models
from django.utils.safestring import mark_safe



class Blog(models.Model):
    img1 =  models.ImageField("img 300px 200px", upload_to=FilenameGenerator(
        prefix='banner'))
    title = models.CharField(max_length=254)
    date = models.DateField(blank=True, null=True)
    short_desc = models.CharField(max_length=254, blank=True, null=True)
    long_desc = models.TextField(blank=True, null=True)
    is_active = models.BooleanField("is published", default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.title

    def preview(self):
        return mark_safe('<a href="/blog/%s" target="_blank"/> preview </a>' % self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super(Blog, self).save()

