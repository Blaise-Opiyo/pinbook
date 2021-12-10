from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User


class NewUserCreationForm(UserCreationForm):

    class Meta:
        model=User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(NewUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'signup-form-input'
        self.fields['password1'].widget.attrs['class'] = 'signup-form-input'
        self.fields['password2'].widget.attrs['class'] = 'signup-form-input'

        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

class NewAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'login-form-input','placeholder': 'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'login-form-input','placeholder':'Password'}))
