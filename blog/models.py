from django.contrib.auth.models import AbstractUser
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'blog'
        verbose_name = 'Blog'


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username


class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'

