# Generated by Django 3.1.2 on 2020-11-22 21:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IgnHeadline',
            fields=[
                ('title', models.CharField(max_length=256)),
                ('img_url', models.URLField(max_length=256)),
                ('news_url', models.URLField(max_length=256, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='StopGameHeadline',
            fields=[
                ('title', models.CharField(max_length=256)),
                ('img_url', models.URLField(max_length=256)),
                ('news_url', models.URLField(max_length=256, primary_key=True, serialize=False)),
            ],
        ),
    ]
