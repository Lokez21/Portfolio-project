from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 150)
    date_posted = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    body_text = models.CharField(max_length = 1500)
