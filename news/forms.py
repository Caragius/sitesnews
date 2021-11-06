from .models import Artical
from django.forms import ModelForm, TextInput, DateTimeField, Textarea, DateTimeInput

class ArticalForm(ModelForm):
    class Meta:
        model = Artical
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'

            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'})
        }
