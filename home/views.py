from django.views.generic import ListView, DetailView, CreateView, UpdateView
from home.models import Question, Answer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404


# class based view for the homepage
class QuestionsView(ListView):
    model = Question
    template_name = "home/index.html"
    # object_list
    # context_object_name = 'questions'
    # ordering = ['-date']


# view a question
class QuestionDetailsView(DetailView):
    model = Question


# view a question
class AnswerDetailsView(DetailView):
    model = Answer


class CreateQuestionView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ["question", "details"]


class UpdateQuestionView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ["question", "details"]

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False


class CreateAnswerView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ["answer"]

    def form_valid(self, form):
        print("\n\n")
        print("question asked is ", self.kwargs["qid"])
        print("\n\n")
        form.instance.question == Question.objects.get(id=self.kwargs["qid"])
        return super().form_valid(form)
