from django.contrib.auth.models import User
from django.db import models


class StopGameHeadline(models.Model):
    desc = models.CharField(max_length=256)
    img_url = models.URLField(max_length=256)
    news_url = models.URLField(max_length=256, primary_key=True)
    id = models.IntegerField(default=None)

    class Meta:
        verbose_name = 'Статья StopGame'
        verbose_name_plural = 'Статьи StopGame'


class IgnHeadline(models.Model):
    title = models.CharField(max_length=256)
    img_url = models.URLField(max_length=256)
    news_url = models.URLField(max_length=256, primary_key=True)
    desc = models.CharField(max_length=256)
    id = models.IntegerField(default=None)

    class Meta:
        verbose_name = 'Статья IGN'
        verbose_name_plural = 'Статьи IGN'
        