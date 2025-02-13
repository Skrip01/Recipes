from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Recipe

User = get_user_model()

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredients',
            instructions='Test Instructions',
        )

    def test_recipe_str(self):
        # Проверяем, что строковое представление рецепта соответствует его названию
        self.assertEqual(str(self.recipe), 'Test Recipe')


class RecipeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredients',
            instructions='Test Instructions',
        )

    def test_recipe_list_view(self):
        # Проверяем, что страница списка рецептов доступна и содержит название созданного рецепта
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)

    def test_recipe_detail_view(self):
        # Проверяем, что детальная страница рецепта возвращает статус 200 и содержит нужные данные
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)
