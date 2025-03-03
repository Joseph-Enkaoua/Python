from django import forms
from app.models import User
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=24,
        widget=forms.TextInput(
            attrs={"placeholder": _("Username"), "class": "form-control"}
        ),
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={"placeholder": _("Password"), "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput(),
        }
        labels = {
            "username": "Username",
            "password": "Password",
        }
        error_messages = {
            "username": {
                "max_length": "Username is too long.",
                "required": "Username is required.",
            },
            "password": {
                "max_length": "Password is too long.",
                "required": "Password is required.",
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not User.exists(username):
            self.add_error("username", _("Username does not exist."))
        else:
            user = User.fetch(username)
            if not user.check_password(password):
                self.add_error("password", _("Incorrect password."))
        return cleaned_data
