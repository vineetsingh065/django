# Generated by Django 3.0.8 on 2020-07-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200720_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='site_name',
            field=models.TextField(default='-'),
        ),
    ]
