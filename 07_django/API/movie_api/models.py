from django.db import models
from faker import Faker
faker = Faker()


class Movie(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                title=faker.catch_phrase()
            )
