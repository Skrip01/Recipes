from django import forms  # Импортируем модуль для работы с формами
from .models import Recipe, Comment, Rating  # Импортируем модель рецепта

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe  # Модель, с которой связана форма
        fields = ['title', 'description', 'ingredients', 'instructions', 'image']
        # Поля, которые будут отображаться в форме

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        # Пользователь вводит только текст комментария;
        # рецепт и автор будут установлены в представлении.

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']
        # Можно добавить атрибуты для поля, чтобы задать HTML-атрибуты (например, min и max)
        widgets = {
            'value': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }