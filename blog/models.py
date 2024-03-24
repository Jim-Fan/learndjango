from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
Blog post model
"""
class Post(models.Model):

    """
    Metadata for django's ORM
    """
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    """
    Enum for post status
    """
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    """
    Model manager for published posts. The book defines this outside of
    Post class but I see no reason of doing so. It is also semantically
    clearer because this class can be used as Post.PublishedManager
    instead of just PublishedManager.
    """
    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    
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

    # Model managers
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title


