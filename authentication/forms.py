from django.contrib.auth import forms


class LoginForm(forms.AuthenticationForm):
    ...


class RegisterForm(forms.UserCreationForm):
    ...
