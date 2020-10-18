from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Settings(models.Model):
    TYPE = (
        ('text_before_service', 'text_before_service'),
        ('about_us_title', 'about_us_title'),
        ('about_us_description', 'about_us_description'),
        ('about_us_img', 'about_us_img'),
        ('our_portfolio_title', 'our_portfolio_title'),
        ('our_portfolio_description', 'our_portfolio_description'),
        ('price_title', 'price_title'),
        ('price_description', 'price_description'),
        ('blog_title', 'blog_title'),
        ('blog_desc', 'blog_desc'),
        ('map_title', 'map_title'),
        ('latitude', 'latitude'),
        ('longitude', 'longitude'),
        ('contact_us_text', 'contact_us_text'),
        ('contact_us_description', 'contact_us_description'),
        ('contact_us_description_2', 'contact_us_description_2'),
        ('address', 'address'),
        ('phone', 'phone'),
        ('email', 'email'),
        ('website', 'website'),
    )
    name = models.CharField(max_length=254, choices=TYPE, unique=True)
    text_value = models.CharField(max_length=254, blank=True, null=True)
    img_value =  models.ImageField(upload_to=FilenameGenerator(
        prefix='settings'))

    def __str__(self):
        return self.name
