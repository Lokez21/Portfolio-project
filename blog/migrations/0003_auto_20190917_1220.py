# Generated by Django 2.2.5 on 2019-09-17 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190913_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 17, 12, 20, 8, 656641), verbose_name='date published'),
        ),
    ]
