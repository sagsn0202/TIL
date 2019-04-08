from django.db import models


class Posting(models.Model):
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.CharField(max_length=20, default='fas fa-question')
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.id}: {self.content[:10]}'


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}: {self.content}'
