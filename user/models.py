import os

from django.contrib.auth.models import User
from django.db import models

from django.core.exceptions import ValidationError


def validate_image(file):
    max_size = 1024 * 1024 * 10  # 10MB
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
    extension = os.path.splitext(file.name)[1][1:].lower()
    if file.size > max_size or extension not in valid_extensions:
        raise ValidationError("Invalid file! Please upload a jpg, jpeg, png, or gif image that is less than 10MB.")


class Profile(models.Model):
    image = models.ImageField(default="default.jpg", upload_to="profileimages", validators=[validate_image])
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"P: {self.user.username}'s profile"

    def delete(self, *args, **kwargs):
        # Delete the image file from the filesystem before deleting the object.
        self.image.delete(save=False)
        super().delete(*args, **kwargs)
