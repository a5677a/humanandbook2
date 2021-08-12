from django.forms import ModelForm
from django import forms

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    class Meta:
        model = Article
        fields = ['title', 'image', 'content']