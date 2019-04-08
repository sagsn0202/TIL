from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    audience = models.IntegerField(default=0)
    open_date = models.DateField()
    genre = models.CharField(max_length=100)
    watch_genre = models.CharField(max_length=100)
    score = models.FloatField(default=0.0)
    poster_url = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title}'
