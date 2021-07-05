from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from home.models import Question, Answer


# class based view for the homepage, lists all the questions in the DB
class QuestionsView(ListView):
    model = Question
    template_name = "home/index.html"
    # object_list
    # context_object_name = 'questions'
    # ordering = ['-date']


# view a question and the answers to the question
class QuestionDetailsView(DetailView):
    model = Question


# view an answer
class AnswerDetailsView(DetailView):
    model = Answer


# add a question
class CreateQuestionView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ["question", "details"]


# update question details
class UpdateQuestionView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ["question", "details"]

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False


# add and answer to a question
class CreateAnswerView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ["answer"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question"] = Question.objects.get(id=self.kwargs["qid"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = Question.objects.get(id=self.kwargs["qid"])
        return super().form_valid(form)
