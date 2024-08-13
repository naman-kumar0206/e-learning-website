from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate

class LoginForm(AuthenticationForm):


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(email=username)
                result = authenticate(username=user.username, password=password)

                if result is not None:
                    return result
                else:
                    raise ValidationError("Email or Password invalid")
            except :
                raise ValidationError("User with this email does not exist")
