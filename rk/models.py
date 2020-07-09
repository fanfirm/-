from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class top_info(models.Model):
    user = models.CharField(max_length=30, verbose_name='客户端号码', unique=True)
    score = models.IntegerField(default=0, verbose_name='分数')

    class Meta:
        verbose_name = '分数以及排行信息'
        verbose_name_plural = verbose_name

