from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel


class Post(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    title = models.CharField(max_length=20, default='')
    content = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
