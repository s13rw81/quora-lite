from django.urls import path, include
from home.views import QuestionsView, QuestionDetailsView, CreateQuestionView
from home.views import UpdateQuestionView, CreateAnswerView, AnswerDetailsView

urlpatterns = [
    path("", QuestionsView.as_view(), name="home"),
    path("answer/<int:pk>/detail/", AnswerDetailsView.as_view(), name="answer-detail"),
    path("answer/<int:qid>/", CreateAnswerView.as_view(), name="add-answer"),
    path("question/<int:pk>/", QuestionDetailsView.as_view(), name="question-detail"),
    path(
        "question/<int:pk>/update/",
        UpdateQuestionView.as_view(),
        name="question-update",
    ),
    path("question/new/", CreateQuestionView.as_view(), name="new-question"),
]
