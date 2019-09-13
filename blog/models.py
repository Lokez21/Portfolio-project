from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 150)
    date_posted = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    body_text = models.TextField(max_length = 1500)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body_text[:100]+'(...)'

    def date_posted_pretty(self):
        return self.date_posted.strftime('%b %e %Y')
