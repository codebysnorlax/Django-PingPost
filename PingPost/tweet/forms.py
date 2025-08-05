from django import forms
from .models import Tweet

class TweetForm(forms.ModelForms):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
