from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Blog post model 
class Post(models.Model):

    # Metadata for django's ORM
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    # Enum
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Keys (self or foreign)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='blog_posts')

    # Fields
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices)

    def __str__(self):
        return self.title