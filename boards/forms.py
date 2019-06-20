from django import forms
from .models import Board, Comment

# class BoardForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'title',
#                 'placeholder': 'Enter the title',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'content-type',
#                 'rows': 5,
#                 'cols': 50,
#                 'placeholder': 'Enter the content',
#             }
#         )
#     )

class BoardForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the title',
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'placeholder': 'Ender the content',
            'rows': 5,
            'cols': 50,
        })
    )

    class Meta: # 데이터를 설명하기 위한 데이터 (메타데이터)
        model = Board
        fields = ('title', 'content',)
        # fields = '__all__'
        # exclude = ('title',)
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'title',
        #     })
        # }

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ('content',)