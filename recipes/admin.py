from django.contrib import admin  # Импортируем модуль admin для работы с админкой
from .models import Recipe  # Импортируем модель Recipe из текущего приложения

admin.site.register(Recipe)  # Регистрируем модель Recipe, чтобы она появилась в админ-панели
