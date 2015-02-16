from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
# Create your models here.

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Email', 'class': 'registerInput'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'First Name','class': 'registerInput'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name','class': 'registerInput'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder':'Username','class': 'registerInput'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password','class': 'registerInput'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password Confirmation','class': 'registerInput'}))

    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        model = User


class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'authInput'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'authInput'}))
 
    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form