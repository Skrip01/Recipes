from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from recipes.models import Recipe

User = get_user_model()

class RecipeAPITest(APITestCase):
    def setUp(self):
        # Создаем пользователя и авторизуем его
        self.user = User.objects.create_user(username='apiuser', password='apipass')
        self.client.login(username='apiuser', password='apipass')
        self.recipe = Recipe.objects.create(
            title='API Test Recipe',
            description='API Description',
            ingredients='API Ingredients',
            instructions='API Instructions',
        )

    def test_get_recipe_list(self):
        # Тестируем получение списка рецептов через API
        url = reverse('recipe-list')  # Название маршрута формируется автоматически роутером
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.recipe.title)
