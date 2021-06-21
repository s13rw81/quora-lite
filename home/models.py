from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
    question = models.CharField(max_length=140, help_text="Enter your question")
    details = models.TextField(
        help_text="provide any additional details", null=True, blank=True
    )
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Q: {self.question} by {self.user.username}"

    def get_absolute_url(self):
        return reverse("question-detail", kwargs={"pk": self.pk})


class Answer(models.Model):
    answer = models.TextField(help_text="add yur answer to the question")
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=2)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"A: {self.answer} by {self.user.username}"

    def get_absolute_url(self):
        return reverse("answer-detail", kwargs={"pk": self.pk})
