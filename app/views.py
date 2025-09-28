from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # правильные адреса генерируем через reverse
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # возвращаем текущее время в удобном формате
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # выводим список файлов рабочей директории
    files = os.listdir(os.getcwd())
    files_list = "<br>".join(files)
    return HttpResponse(f"<h3>Содержимое рабочей директории:</h3><p>{files_list}</p>")
