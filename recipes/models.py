from django.db import models  # Импортируем модуль models для создания моделей
from django.conf import settings  # Для ссылки на модель пользователя
from django.core.validators import MinValueValidator, MaxValueValidator

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

    image = models.ImageField(
        upload_to='recipes/',
        null=True,
        blank=True,
        help_text="Загрузите изображение рецепта"
    )

    def __str__(self):
        # Этот метод определяет строковое представление объекта, что удобно для отображения в админке и консоли.
        return self.title  # возвращаем название рецепта

class Comment(models.Model):
    recipe = models.ForeignKey(
        'Recipe',
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at: автоматически сохраняет дату и время создания комментария

    def __str__(self):
        return f'Комментарий от {self.author} к {self.recipe}'

class Rating(models.Model):
    DoesNotExist = None
    objects = None
    recipe = models.ForeignKey(
        'Recipe',
        related_name='ratings',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    value = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'author')  # Каждый пользователь может оценить рецепт только один раз

    def __str__(self):
        return f"{self.value} by {self.author} for {self.recipe}"