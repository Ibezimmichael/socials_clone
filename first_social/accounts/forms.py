from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = 'Display name'
        self.fields["email"].label = "Email address"
        self.fields['username'].widget.attrs.update({'class': 'w-50'})
        self.fields['email'].widget.attrs.update({'class': 'w-50'})
        self.fields['password1'].widget.attrs.update({'class': 'w-50'})
        self.fields['password2'].widget.attrs.update({'class': 'w-50'})
        self.fields['profile_pic'].widget.attrs.update({'class': 'w-50'})


