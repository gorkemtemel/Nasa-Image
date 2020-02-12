from django.shortcuts import render, HttpResponse
from .models import nasa_default_image

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim': 'GÖRKEM',
            'img':nasa_default_image()
        }
    else:
        context = {
            'isim': 'Misafir Kullanıcı',
            'img':''
        }
    return render(request, 'home.html', context)
