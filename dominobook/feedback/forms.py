from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)  # widget=forms.Textarea для ввода многострочного текста, после каждой строчки ставится /n
