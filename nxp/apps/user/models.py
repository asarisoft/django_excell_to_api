from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def create_user(self, username, password, **extra_fields):
        now = timezone.now()
        user = self.model(
            username=username,
            is_active=True, is_superuser=False,
            last_login=now, **extra_fields)

        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('Status Staff', default=False)
    mobile_number = models.CharField(max_length=30, default='', blank=True)
    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return '%s - %s' % (self.username, self.name)

    def __unicode__(self):
        return '%s - %s' % (self.username, self.name)

    def serialize(self):
        return  {
            "username" : self.username,
            "name" : self.name,
            "mobile_number" : self.mobile_number,
        }

    # def save(self, *args, **kwargs):
    #     exist_id = self.id
    #     super(User, self).save(*args, **kwargs)

    #     self.kabupaten = Kabupaten.objects.first()
    #     self.provinsi = Provinsi.objects.first()
        
    #     if not exist_id:
    #         self.order = get_next_value("order_user")
    #         PrintCard.objects.create(user=self, order=self.order)
    #         self.save()
