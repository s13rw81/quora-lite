from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    image = models.ImageField(default="default.jpg", upload_to="profileimages")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"P: {self.user.username}'s profile"
