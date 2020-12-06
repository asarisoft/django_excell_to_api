from nxp.core.utils import FilenameGenerator
from django.db import models


class Settings(models.Model):
    TYPE = (
        ('about_us_background', 'about_us_background'),
        ('about_us_description', 'about_us_description'),
        ('about_us_img', 'about_us_img'),
        ('about_us_title', 'about_us_title'),

        ('address', 'address'),

        ('blog_desc', 'blog_desc'),
        ('blog_title', 'blog_title'),
        
        ('contact_us_title', 'contact_us_title'),
        ('contact_us_description', 'contact_us_description'),
        ('contact_us_description_2', 'contact_us_description_2'),
        
        ('email', 'email'),
        ('facebook_url', 'facebook_url'),
        ('favicon', 'favicon'),
        ('instagram_url', 'instagram_url'),

        ('latitude', 'latitude'),
        ('longitude', 'longitude'),
        ('logo', 'logo'),

        ('our_portfolio_title', 'our_portfolio_title'),
        ('our_portfolio_description', 'our_portfolio_description'),

        ('our_team_title', 'our_team_title'),
        ('our_team_description', 'our_team_description'),

        ('our_service_title', 'our_service_title'),
        ('our_service_description', 'our_service_description'),
        
        ('testimoni_title', 'testimoni_title'),
        ('testimoni_background', 'testimoni_background'),
        
        ('phone', 'phone'),
        ('price_title', 'price_title'),
        ('price_description', 'price_description'),

        ('seo_description', 'SEO Description'),
        ('seo_title', 'SEO Title'),
        ('seo_keywords', 'SEO Keywords'),
        ('seo_image', 'SEO Image'),
        # ('seo_fb_id', 'SEO FbID'),
        
        ('text_before_service', 'text_before_service'),
        ('twitter_url', 'twitter_url'),
        
        ('website', 'website'),
        
        ('youtube_url', 'youtube_url'),
    )
    name = models.CharField(max_length=254, choices=TYPE, unique=True)
    text_value = models.TextField(blank=True, null=True)
    img_value =  models.ImageField(upload_to=FilenameGenerator(
        prefix='settings'), blank=True, null=True)

    def __str__(self):
        return self.name
