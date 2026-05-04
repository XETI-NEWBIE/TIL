from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'field-input',
                'placeholder': '이름을 비우면 익명으로 등록됩니다.',
            }
        ),
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'field-input',
                    'placeholder': '예: KOSPI 추가 매수 시점을 어떻게 보시나요?',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'field-input field-textarea',
                    'placeholder': '시장 흐름, 리스크, 투자 아이디어를 자유롭게 남겨보세요.',
                }
            ),
        }

    def clean_author(self):
        return self.cleaned_data['author'].strip() or '익명'
