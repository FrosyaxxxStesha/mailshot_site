from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, \
    UserChangeForm
from django.forms import ModelForm, HiddenInput

from services.general.form_mixins import FormControlMixin

User = get_user_model()


class RegistrationForm(FormControlMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', "password1", "password2")


class LoginForm(FormControlMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserUpdateForm(FormControlMixin, ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'telephone_number', 'first_name', 'last_name')


class UserPasswordResetForm(FormControlMixin, PasswordResetForm):
    pass


class UserSetPasswordForm(FormControlMixin, SetPasswordForm):
    pass


class DeactivateUserForm(FormControlMixin, ModelForm):
    class Meta:
        model = User
        fields = ("is_active",)
        widgets = {
            "is_active": HiddenInput()
        }
