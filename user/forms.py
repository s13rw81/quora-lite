from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import Profile


class Register(UserCreationForm):
    first_name = forms.CharField(
        label="Enter your First Name", max_length=20, required=True
    )
    middle_name = forms.CharField(
        label="Enter your Middle Name", max_length=20, required=False
    )
    last_name = forms.CharField(
        label="Enter your Last Name", max_length=20, required=True
    )
    email = forms.EmailField(label="Enter your Email", required=True)

    image = forms.ImageField(label="Upload Display Picture", required=False)

    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
            "image"
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if self.cleaned_data.get('image'):
                profile = Profile.objects.create(user=user, image=self.cleaned_data.get('image'))
                profile.save()
        return user

