from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    # Python의 Inner class라는 문법과 무관.
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)