from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView
from user.forms import Register


def register(request):
    if request.method == "POST":
        form = Register(request.POST)
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
    fields = ["first_name", "last_name", "username", "email"]
    # template_name = 'user/update_profile.html'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False

    def get_success_url(self):
        return reverse("profile")
