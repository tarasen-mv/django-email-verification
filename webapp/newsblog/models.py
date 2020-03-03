from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    image = models.BooleanField(default=False)

    @property
    def short_text(self):
        return self.author + self.title

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.author + self.text[:50] + '...'
