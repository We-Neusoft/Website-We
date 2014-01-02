from django import forms

class InitializationForm(forms.Form):
    response_type = forms.SlugField()
    client_id = forms.SlugField()
    redirect_uri = forms.URLField(required=False)
    scope = forms.CharField(required=False)
    state = forms.SlugField(required=False)

class AuthenticationForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField()
