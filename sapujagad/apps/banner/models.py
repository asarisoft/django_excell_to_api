from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Banner(models.Model):
    img =  models.ImageField(upload_to=FilenameGenerator(
        prefix='banner'))
    big_text = models.CharField(max_length=254, blank=True, null=True)
    small_text = models.CharField(max_length=254, blank=True, null=True)
    url = models.CharField(max_length=254, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    # owner = models.ForeignKey('user.User', on_delete=models.CASCADE)
    # kecamatan = models.ForeignKey(
    #     'kecamatan.Kecamatan', on_delete=models.SET_NULL, blank=True, null=True)
    # kelurahan = models.ForeignKey(
    #     'kelurahan.Kelurahan', on_delete=models.SET_NULL, blank=True, null=True)
    # liked_by = models.ManyToManyField('user.User', blank=True, related_name='likes_by')
    # seen_by = models.ManyToManyField('user.User', blank=True, related_name='seens_by')
    # expired = models.DateField('expired', blank=True, null=True)
    # created = AutoCreatedField()
    # price = models.IntegerField(default=0)
    # wa_number = models.CharField('Wa Number', max_length=30, blank=True, null=True)

    def __str__(self):
        return self.big_text
