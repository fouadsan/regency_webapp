from django import forms
from .models import Signup


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Signup
        fields = ('email', )