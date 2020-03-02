from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'inputUsername',
                'class': 'form-control',
                'placeholder': 'Username',
                'required': True
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'id': 'inputPassword',
                'class': 'form-control',
                'placeholder': 'Password',
                'required': True
            }
        ),
        # validators=[self.is_user_exists]
    )

    # def is_user_exists(self, value):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #
    #     try:
    #         user = User.objects.get(username=username)
    #
    #     except User.DoesNotExist:
    #         raise ValidationError({'username': 'Not exist'})
    #
    #     if not user.check_password(password):
    #         raise ValidationError({'password': 'wrong'})


class AddUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'inputUsername',
                'class': 'form-control',
                'placeholder': 'Username',
                'required': True
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'id': 'inputPassword',
                'class': 'form-control',
                'placeholder': 'Password',
                'required': True
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'id': 'inputEmail',
                'class': 'form-control',
                'placeholder': 'Email address',
                'required': True
            }
        )
    )
