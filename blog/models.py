from django.db import models
import django
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 150)
    # date_posted = models.DateTimeField("date published", default=datetime.datetime.now())
    date_posted = models.DateField(default=django.utils.timezone.now)
    image = models.ImageField(upload_to = 'images/')
    # body_text = models.TextField(max_length = 1500)
    body_text = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body_text[:100]+'(...)'

    def date_posted_pretty(self):
        return self.date_posted.strftime('%b %e %Y')
