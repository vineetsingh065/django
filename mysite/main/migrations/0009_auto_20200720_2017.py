# Generated by Django 3.0.8 on 2020-07-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200720_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='site_name',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
