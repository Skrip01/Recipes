from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    # Используем стандартное представление LoginView с указанием шаблона
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # LogoutView выполняет выход и перенаправление (параметр next_page указывает адрес перенаправления)
    path('logout/', auth_views.LogoutView.as_view(next_page='recipe_list'), name='logout'),
]
