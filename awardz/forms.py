from django.contrib.auth.models import User
from django import forms
from .models import Project_Post,Reviews,Profile




class SignUpForm(User):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )