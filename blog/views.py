from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DetailView
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse("blog-detail", kwargs={"id": self.id})
