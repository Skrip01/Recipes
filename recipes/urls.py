from django.urls import path  # Импортируем функцию path для определения маршрутов
from .views import recipe_list, recipe_detail, recipe_create, recipe_update, recipe_delete, \
    comment_create, rating_create  # Импортируем наше представление

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    # При обращении к корню нашего приложения ('') вызывается функция recipe_list
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    # При обращении по адресу /recipe/номер/ вызывается recipe_detail, где номер – pk рецепта
    path('recipe/create/', recipe_create, name='recipe_create'),
    # Новый маршрут для создания рецепта
    path('recipe/<int:pk>/update/', recipe_update, name='recipe_update'),
    # Добавлен маршрут для редактирования рецепта
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
    # Маршрут для удаления
    path('recipe/<int:pk>/comment/', comment_create, name='comment_create'),
    path('recipe/<int:pk>/rate/', rating_create, name='rating_create'),
]
