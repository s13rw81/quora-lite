from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView, DeleteView
from user.forms import Register


def register(request):
    if request.method == "POST":
        form = Register(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"Account created for {username}")
            return redirect("login")
        else:
            form = Register(request.POST)
            return render(
                request, template_name="user/register.html", context={"form": form}
            )

    else:
        form = Register()
        return render(
            request, template_name="user/register.html", context={"form": form}
        )


@login_required
def profile(request):
    print("\n\n")
    print(request.user.first_name)
    print(request.user.last_name)
    print(request.user.email)
    print("\n\n")
    return render(request, template_name="user/profile.html")


def login(request):
    form = AuthenticationForm()
    return render(request, template_name="user/login.html", context={"form": form})


class UpdateProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ["first_name", "last_name", "username", "email", "image"]

    # template_name = 'user/update_profile.html'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False

    def get_success_url(self):
        return reverse("profile")


class DeleteProfileView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User

    def form_valid(self, form):
        messages.success(self.request, "The account was deleted successfully.")
        return super(DeleteProfileView, self).form_valid(form)

    def get_success_url(self):
        return reverse("home")

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            # display = user.profile.image
            # print("you need to delete display image at ", display)
            # path_to_dp = os.path.join(BASE_DIR, 'media', display)
            # try:
            #     os.remove(path_to_dp)
            # except Exception as e:
            #     print(e)
            return True
        return False
