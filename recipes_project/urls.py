"""
URL configuration for recipes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin  # Импортируем админку
from django.urls import path, include  # Функция include позволяет подключать маршруты других приложений

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для админ-панели
    path('', include('recipes.urls')),  # Подключаем маршруты приложения recipes к корню сайта
    path('accounts/', include('accounts.urls')), # Подключаем регистрацию
    path('api/', include('recipes.api_urls')),  # API доступен по префиксу /api/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
