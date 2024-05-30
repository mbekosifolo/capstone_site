from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime


class Category(models.Model):
    name = models.CharField(max_length=255, default='uncategorized')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Home')


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = QuillField(default='Content here')
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    image_alt = models.CharField(max_length=140)
    category = models.CharField(max_length=255, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title + ' by ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article', args=[self.id])

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)