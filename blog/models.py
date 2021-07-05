from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    content = models.TextField(verbose_name="Post ", unique=True)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=140, verbose_name="Post Title ", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"P.{self.id} by {self.user.username}"

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
