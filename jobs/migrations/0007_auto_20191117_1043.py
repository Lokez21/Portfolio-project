# Generated by Django 2.2.5 on 2019-11-17 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_job_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['position'], 'verbose_name': 'Job', 'verbose_name_plural': 'Job'},
        ),
    ]
