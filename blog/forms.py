from django import forms
from .models import NewsBlog
import re
from django.core.exceptions import ValidationError


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = NewsBlog
        fields = ('title', 'news_text')

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название должно начинаться с буквы!')
        return title