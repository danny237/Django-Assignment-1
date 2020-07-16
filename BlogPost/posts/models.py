from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name          = models.CharField(max_length=100)
    last_name           = models.CharField(max_length=100)
    email               = models.EmailField()
    username            = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Posts(models.Model):
    title               = models.SlugField(max_length=250)
    content             = models.TextField()
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    author              = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name_plural='Post'

