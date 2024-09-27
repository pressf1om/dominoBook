from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите почту'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
        }
