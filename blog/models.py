from django.db import models
from django.contrib.auth.models import User


class article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="articles/")
    pub_date = models.DateTimeField(auto_now_add=True)
    Update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.content[:30]}"
