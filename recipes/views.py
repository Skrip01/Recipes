from django.shortcuts import render, get_object_or_404, redirect  # Функция render помогает отображать шаблоны
from .models import Recipe  # Импортируем модель Recipe для работы с данными
from .forms import RecipeForm  # Импортируем форму для создания рецепта

def recipe_list(request):
    recipes = Recipe.objects.all()
    # Получаем все объекты модели Recipe из базы данных
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
    # Рендерим шаблон recipe_list.html и передаём в него словарь с рецептами

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    # Получаем объект рецепта по его первичному ключу (pk) или возвращаем 404, если рецепт не найден
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
    # Рендерим шаблон recipe_detail.html и передаём в него рецепт

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        # Если форма отправлена методом POST, заполняем её данными из запроса
        if form.is_valid():
            form.save()  # Сохраняем новый рецепт в базе данных
            return redirect('recipe_list')  # Перенаправляем пользователя к списку рецептов
    else:
        form = RecipeForm()  # Если запрос GET, создаем пустую форму для заполнения
    return render(request, 'recipes/recipe_create.html', {'form': form})
    # Рендерим шаблон для создания рецепта и передаем форму в контексте