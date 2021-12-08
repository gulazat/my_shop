from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    nickname = models.CharField(blank=True, null=True, max_length=20)
    avatar = models.FileField(upload_to='avatar/')
    mobile = models.CharField(blank=True, null=True, max_length=13)
    subscribe = models.BooleanField(default=False)
    introduction = models.TextField()
    staff_status = models.BooleanField(default=False)

    class Meta:
        db_table = 'refist_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name