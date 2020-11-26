# Generated by Django 3.1.2 on 2020-11-24 19:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0004_auto_20201124_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='headline',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.CreateModel(
            name='Comment_StopGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_sg',
                                             to=settings.AUTH_USER_MODEL)),
                ('headline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_sg',
                                               to='games.stopgameheadline')),
            ],
            options={
                'verbose_name': 'Комментарий StopGame',
                'verbose_name_plural': 'Комментарии StopGame',
            },
        ),
        migrations.CreateModel(
            name='Comment_IGN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_ign',
                                             to=settings.AUTH_USER_MODEL)),
                ('headline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_ign',
                                               to='games.ignheadline')),
            ],
            options={
                'verbose_name': 'Комментарий IGN',
                'verbose_name_plural': 'Комментарии IGN',
            },
        ),
    ]
