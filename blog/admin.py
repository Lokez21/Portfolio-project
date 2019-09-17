from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):

    fieldsets = [
                ("Title/Date", {"fields": ["title", "date_posted"]}),
                ("Content", {"fields":["image", "body_text"]})
    ]


admin.site.register(Blog, BlogAdmin)
