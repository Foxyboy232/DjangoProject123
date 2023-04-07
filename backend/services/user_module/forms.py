from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class ProfileForm(forms.ModelForm):
    password_old = forms.CharField(required=False)
    password_new = forms.CharField(required=False)
    class Meta:
        fields = ("first_name", "last_name", "username", "password", "password_new", "password_old")

class AuthForm(forms.Form):
    class Meta:
        fields = ("username", "password")