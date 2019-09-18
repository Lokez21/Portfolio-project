from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 100, null=True, blank=True)
    summary = models.CharField(max_length = 200)
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.summary
