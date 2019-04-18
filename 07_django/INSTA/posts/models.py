from django.db import models
from django_extensions.db.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

from os import environ
ENV = environ.get('ENVIRONMENT', 'DEVELOPMENT')
if ENV == 'DEVELOPMENT':
    from IPython import embed
    from faker import Faker
    faker = Faker()


class Post(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    content = models.CharField(max_length=210)

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            Post.objects.create(content=faker.text(210))


class Image(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
        blank=True,
        upload_to='posts/images',
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={'quality': 90}
    )


class Comment(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
