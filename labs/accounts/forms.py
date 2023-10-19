from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].widget = forms.HiddenInput()