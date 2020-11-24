from django.contrib.auth.models import User
from django.db import models


class StopGameHeadline(models.Model):
    desc = models.CharField(max_length=256, )
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


class Comment_StopGame(models.Model):
    headline = models.ForeignKey(StopGameHeadline, related_name="comments_sg", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="author_sg", on_delete=models.CASCADE)
    text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Комментарий StopGame"
        verbose_name_plural = "Комментарии StopGame"


class Comment_IGN(models.Model):
    headline = models.ForeignKey(IgnHeadline, related_name="comments_ign", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="author_ign", on_delete=models.CASCADE)
    text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Комментарий IGN"
        verbose_name_plural = "Комментарии IGN"

class Comment(models.Model):
    pass