from django import forms  # Импортируем модуль для работы с формами
from .models import Recipe  # Импортируем модель рецепта

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe  # Модель, с которой связана форма
        fields = ['title', 'description', 'ingredients', 'instructions']
        # Поля, которые будут отображаться в форме
