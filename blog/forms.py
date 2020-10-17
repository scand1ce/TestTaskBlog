from django import forms
from .models import New


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('title', 'news_text')

