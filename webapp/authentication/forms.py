from django import forms

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
        )
    )


class AddUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'id': 'inputEmail',
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
