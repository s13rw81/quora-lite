from blog.models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# TODO: improve CSS of PostDetailView
# TODO: add link to return to PostListView on PostDetailsView
# TODO: make new blog button visible on all pages


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


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = 'blog/post_update_form.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    # success_url = reverse("blog-home", urlconf='blog.urls')

    def form_valid(self, form):
        messages.success(self.request, "The post was deleted successfully.")
        return super(PostDeleteView, self).form_valid(form)

    def get_success_url(self):
        return reverse("blog-home")
