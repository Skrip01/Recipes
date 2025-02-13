from django.db import models  # Импортируем модуль models для создания моделей

class Recipe(models.Model):  # Создаем класс Recipe, который наследует от models.Model
    objects = None
    title = models.CharField(max_length=200)
    # title: название рецепта. CharField — строковое поле, max_length=200 задаёт максимальную длину

    description = models.TextField()
    # description: краткое описание рецепта. TextField подходит для больших текстов

    ingredients = models.TextField()
    # ingredients: список ингредиентов. TextField для ввода большого количества текста

    instructions = models.TextField()
    # instructions: пошаговая инструкция по приготовлению

    created_at = models.DateTimeField(auto_now_add=True)
    # created_at: дата и время создания записи. auto_now_add=True означает, что поле заполняется автоматически при создании

    def __str__(self):
        # Этот метод определяет строковое представление объекта, что удобно для отображения в админке и консоли.
        return self.title  # возвращаем название рецепта
