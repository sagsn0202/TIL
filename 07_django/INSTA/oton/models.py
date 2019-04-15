from django.db import models
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel


class MagazineArticle(TitleDescriptionModel, TimeStampedModel):
    content = models.TextField()


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Writer(TimeStamp):
    name = models.CharField(max_length=20, default='', unique=True)


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, default='', unique=True)
    description = models.TextField(default='')


class Chapter(TitleDescriptionModel, TimeStampedModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
