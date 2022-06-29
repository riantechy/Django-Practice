from django.contrib import admin
from .models import Post

#giving the admin the permission to Query the Posts.
admin.site.register(Post)
