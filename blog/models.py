from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#creating tables for the posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #thunder str method which tells us how the data should be printed.
    def __str__(self):
        return self.title
