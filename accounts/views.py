from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return HttpResponseRedirect('/')
        else:
            # Отображение страницы с ошибкой
            return HttpResponse("не саксес")
    else:
        return render(request, 'accounts/login.html')

