from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.


def posts(request):
    return HttpResponse('Все посты блога')


def index(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def get_info_post(request, name_post):
    return HttpResponse(f'Здесь содержится информация о посте под номером {name_post}')


def get_number_post(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
