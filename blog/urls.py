from blog import views
from django.urls import path, include

urlpatterns = [
    # path("delete/", views.home, name="blog-delete"),
    # path("update/", views.home, name="blog-update"),
    path("", views.PostListView.as_view(), name="blog-home"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="blog-detail"),
    path("new/", views.PostCreateView.as_view(), name="blog-create"),
]
