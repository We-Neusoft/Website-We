from django import forms

class InitializationForm(forms.Form):
    response_type = forms.SlugField()
    client_id = forms.SlugField()
    redirect_uri = forms.URLField(required=False)
    scope = forms.CharField(required=False)
    state = forms.SlugField(required=False)

class AuthenticationForm(forms.Form):
    action = forms.SlugField()
    username = forms.EmailField(required=False)
    password = forms.CharField(required=False)
