# Generated by Django 2.2.5 on 2019-09-18 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190917_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 18, 11, 47, 0, 223167), verbose_name='date published'),
        ),
    ]
