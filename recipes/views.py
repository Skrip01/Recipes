from django.shortcuts import render, get_object_or_404, redirect  # Функция render помогает отображать шаблоны
from .models import Recipe, Rating  # Импортируем модель Recipe для работы с данными
from .forms import RecipeForm, CommentForm, RatingForm  # Импортируем форму для создания рецепта
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    all_recipes = Recipe.objects.all().order_by('-created_at')
    # Создаем объект Paginator: 5 рецептов на страницу
    paginator = Paginator(all_recipes, 5)

    # Получаем номер текущей страницы из GET-параметров
    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)

    # Рендерим шаблон списка рецептов, передавая объект с рецептами
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    # Получаем объект рецепта по его первичному ключу (pk) или возвращаем 404, если рецепт не найден
    ratings = recipe.ratings.all()
    average_rating = None
    if ratings.exists():
        total = sum(r.value for r in ratings)
        average_rating = total / ratings.count()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
    # Рендерим шаблон recipe_detail.html и передаём в него рецепт

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES) # Передаем request.FILES для обработки файлов
        # Если форма отправлена методом POST, заполняем её данными из запроса
        if form.is_valid():
            form.save()  # Сохраняем новый рецепт в базе данных
            return redirect('recipe_list')  # Перенаправляем пользователя к списку рецептов
    else:
        form = RecipeForm()  # Если запрос GET, создаем пустую форму для заполнения
    return render(request, 'recipes/recipe_create.html', {'form': form})
    # Рендерим шаблон для создания рецепта и передаем форму в контексте


def recipe_update(request, pk):
    # Получаем объект рецепта по его первичному ключу (pk)
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        # Если форма отправлена методом POST, создаем форму с данными и привязываем к существующему рецепту
        form = RecipeForm(request.POST,request.FILES, instance=recipe)  # Добавили request.FILES
        if form.is_valid():
            # Если данные валидны, сохраняем изменения в базе данных
            form.save()
            # Перенаправляем на детальную страницу рецепта после сохранения
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        # При GET-запросе создаем форму, предзаполненную данными рецепта
        form = RecipeForm(instance=recipe)

    # Рендерим шаблон для редактирования рецепта и передаем в него форму и объект рецепта
    return render(request, 'recipes/recipe_update.html', {'form': form, 'recipe': recipe})


def recipe_delete(request, pk):
    # Получаем объект рецепта по его первичному ключу
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        # При подтверждении удаления (POST-запрос) удаляем рецепт
        recipe.delete()
        # Перенаправляем на список рецептов после удаления
        return redirect('recipe_list')

    # Рендерим шаблон с запросом на подтверждение удаления
    return render(request, 'recipes/recipe_delete.html', {'recipe': recipe})

@login_required  # Требуем, чтобы пользователь был авторизован
def comment_create(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # Устанавливаем связи с рецептом и автором
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            # После сохранения перенаправляем пользователя на детальную страницу рецепта
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = CommentForm()
    return render(request, 'recipes/comment_create.html', {'form': form, 'recipe': recipe})


@login_required
def rating_create(request, pk):
    # Получаем рецепт, для которого ставится оценка
    recipe = get_object_or_404(Recipe, pk=pk)

    # Пытаемся получить уже существующую оценку данного рецепта от текущего пользователя
    try:
        rating = Rating.objects.get(recipe=recipe, author=request.user)
    except Rating.DoesNotExist:
        rating = None

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.recipe = recipe
            rating.author = request.user
            rating.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RatingForm(instance=rating)

    return render(request, 'recipes/rating_create.html', {'form': form, 'recipe': recipe})


