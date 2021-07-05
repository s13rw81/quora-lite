from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=140, verbose_name="Post Title ", unique=True)
    content = models.TextField(verbose_name="Post ", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"P.{self.id} by {self.user.username}"

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
