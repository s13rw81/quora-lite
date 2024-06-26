from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Question(models.Model):
    date = models.DateTimeField(auto_now=True)
    details = models.TextField(
        help_text="provide any additional details", null=True, blank=True
    )
    question = models.CharField(
        max_length=140, help_text="Enter your question", unique=True
    )
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # TODO : add ENUMs to specify status of question [OPEN, DELETED, CLOSED]

    def __str__(self):
        return f"Q: {self.question} by {self.user.username}"

    def get_absolute_url(self):
        return reverse("question-detail", kwargs={"pk": self.pk})


class Answer(models.Model):
    answer = models.TextField(help_text="add your answer to the question", unique=True)
    date = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=2)

    def __str__(self):
        return f"A: {self.answer} by {self.user.username}"

    def get_absolute_url(self):
        return reverse("answer-detail", kwargs={"pk": self.pk})
