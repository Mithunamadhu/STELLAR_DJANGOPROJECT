from django import forms
from .models import Contact
from django.contrib.auth.forms import AuthenticationForm, UsernameField
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'location']

class CustomLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your email',
        'autocomplete': 'username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your password',
        'autocomplete': 'current-password',
    }))

    error_messages = {
        'invalid_login': 'Oops—email or password didn’t match!',
        'inactive': 'This account is inactive.',
    }
