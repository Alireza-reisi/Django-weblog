from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class article(models.Model):
    POST = None
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="articles/")
    pub_date = models.DateTimeField(auto_now_add=True)
    Update_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, null=True)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"title": self.title})

    def __str__(self):
        return self.title
