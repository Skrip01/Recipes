from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        # При отправке формы создаем экземпляр UserCreationForm с данными из POST-запроса
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Если форма валидна, сохраняем нового пользователя
            user = form.save()
            # Автоматически авторизуем пользователя после регистрации
            login(request, user)
            # Перенаправляем на главную страницу рецептов
            return redirect('recipe_list')
    else:
        # Если запрос GET, создаем пустую форму для регистрации
        form = UserCreationForm()
    # Рендерим шаблон регистрации и передаём форму в контексте
    return render(request, 'accounts/register.html', {'form': form})
