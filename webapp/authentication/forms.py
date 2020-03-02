from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
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
