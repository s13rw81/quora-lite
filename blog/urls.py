from django.urls import path, include
from blog import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="blog-home"),
    path("new/", views.PostCreateView.as_view(), name="blog-create"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="blog-detail"),
    # path("update/", views.home, name="blog-update"),
    # path("delete/", views.home, name="blog-delete"),
]
