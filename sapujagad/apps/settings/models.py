from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Settings(models.Model):
    TYPE = (
        ('text_before_service', 'text_before_service'),
        ('about_us_title', 'about_us_title'),
        ('about_us_description', 'about_us_description'),
        ('about_us_img', 'about_us_img'),
        ('about_us_background', 'about_us_background'),
        ('our_portfolio_title', 'our_portfolio_title'),
        ('our_portfolio_description', 'our_portfolio_description'),
        ('our_service_title', 'our_service_title'),
        ('our_service_description', 'our_service_description'),
        ('our_team_title', 'our_team_title'),
        ('our_team_description', 'our_team_description'),
        ('price_title', 'price_title'),
        ('price_description', 'price_description'),
        ('blog_title', 'blog_title'),
        ('blog_desc', 'blog_desc'),
        ('contact_us_title', 'contact_us_title'),
        ('contact_us_description', 'contact_us_description'),
        ('contact_us_description_2', 'contact_us_description_2'),
        ('address', 'address'),
        ('phone', 'phone'),
        ('email', 'email'),
        ('website', 'website'),
        ('logo', 'logo'),
        ('themium_title', 'themium_title'),
        ('instagram_url', 'instagram_url'),
        ('facebook_url', 'facebook_url'),
        ('youtube_url', 'youtube_url'),
        ('twitter_url', 'twitter_url'),

    )
    name = models.CharField(max_length=254, choices=TYPE, unique=True)
    text_value = models.TextField(blank=True, null=True)
    img_value =  models.ImageField(upload_to=FilenameGenerator(
        prefix='settings'), blank=True, null=True)

    def __str__(self):
        return self.name
