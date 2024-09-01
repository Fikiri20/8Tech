from django import forms


class ResetPasswordEmailCollection(forms.Form):
    email = forms.EmailField(max_length=255)


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)