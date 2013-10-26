from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(max_length=32)
    domain = forms.CharField(max_length=16)
    password = forms.CharField(max_length=32)
