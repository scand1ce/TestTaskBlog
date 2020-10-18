from django import forms
from django.forms import Textarea
from .models import New


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('title', 'news_text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['news_text'].widget = Textarea(attrs={'rows': 5})

