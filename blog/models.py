from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#creating tables for the posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #thunder str method which tells us how the data should be printed.
    def __str__(self):
        return self.title


    # directing the user after creating the post to another page
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
