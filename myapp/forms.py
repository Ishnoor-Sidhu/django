# myapp/forms.py
from django import forms
from .models import Registeration
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = Registeration
        fields = ('username', 'email')  # exclude password field from form

    def clean_password2(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if not p1 or p1 != p2:
            raise ValidationError("Passwords do not match.")
        return p2
