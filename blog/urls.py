from blog import views
from django.urls import path

urlpatterns = [
    path("", views.PostListView.as_view(), name="blog-home"),
    path("new/", views.PostCreateView.as_view(), name="blog-create"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="blog-detail"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="blog-update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="blog-delete"),
]
