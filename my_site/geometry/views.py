from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def get_rectangle_area(request, width, height: str):
    area = width * height
    return HttpResponse(f'Площадь прямоуголника размером {width}x{height} равна {area}')


def get_square_area(request, width: int):
    area = width ** 2
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {area}')


def get_circle_area(request, radius: int):
    area = 3.14 * radius ** 2
    return HttpResponse(f'Площадь круга радиуса {radius} равна {area}')


def rectangle(request, width, height: str):
    area = width * height
    redirect_url = reverse('rectangle_name', args=(width, height))
    return HttpResponseRedirect(redirect_url)
    # return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def square(request, width: int):
    area = width ** 2
    redirect_url = reverse('square_name', args=(width,))
    return HttpResponseRedirect(redirect_url)
    # return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def circle(request, radius: int):
    area = 3.14 * radius ** 2
    redirect_url = reverse('circle_name', args=(radius,))
    return HttpResponseRedirect(redirect_url)
    # return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
