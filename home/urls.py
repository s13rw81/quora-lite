from django.urls import path
from home.views import QuestionsView, QuestionDetailsView, CreateQuestionView, QuestionDeleteView
from home.views import UpdateQuestionView, CreateAnswerView, AnswerDetailsView

urlpatterns = [
    path("", QuestionsView.as_view(), name="home"),
    path("answer/<int:pk>/detail/", AnswerDetailsView.as_view(), name="answer-detail"),
    path("answer/<int:qid>/new/", CreateAnswerView.as_view(), name="add-answer"),
    path("question/<int:pk>/", QuestionDetailsView.as_view(), name="question-detail"),
    path("question/<int:pk>/update/", UpdateQuestionView.as_view(), name="question-update",),
    path("question/<int:pk>/delete/", QuestionDeleteView.as_view(), name="question-delete",),
    path("question/new/", CreateQuestionView.as_view(), name="new-question"),
]
