# Generated by Django 2.2.5 on 2019-09-30 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190929_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
