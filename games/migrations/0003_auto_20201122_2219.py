# Generated by Django 3.1.2 on 2020-11-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20201122_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='ignheadline',
            name='id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='stopgameheadline',
            name='id',
            field=models.IntegerField(default=None),
        ),
    ]