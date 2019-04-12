from django.db import models
from os import environ
ENV = environ.get('ENVIRONMENT', 'DEVELOPMENT')
if ENV == 'DEVELOPMENT':
    from IPython import embed
    from faker import Faker
    faker = Faker()


class Post(models.Model):
    content = models.CharField(max_length=210)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            Post.objects.create(content=faker.text(210))
